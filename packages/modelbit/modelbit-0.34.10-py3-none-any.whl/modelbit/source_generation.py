from .helpers import RuntimePythonProps, JobProps, InstancePickleWrapper
from typing import List, Optional

DefaultModuleName = "source"


class RuntimeFile:

  def __init__(self, name: str, contents: str):
    self.name = name
    self.contents = contents

  def asDict(self):
    return {"name": self.name, "contents": self.contents}


def _addSpacer(strList: List[str]):
  if len(strList) > 0 and strList[-1] != "":
    strList.append("")


def _loadEnvVarSecretLine(envVar: str) -> str:
  return f'os.environ["{envVar}"] = modelbit.get_secret("{envVar}", ignore_missing=True)'


def sourceForLoadingSecrets(integrationEnvVars: Optional[List[str]]) -> Optional[str]:
  if integrationEnvVars is None or len(integrationEnvVars) == 0:
    return None

  lines: List[str] = []
  for iev in integrationEnvVars:
    lines.append(_loadEnvVarSecretLine(iev))
  return "\n".join(lines)


def makeSourceFile(pyProps: RuntimePythonProps,
                   sourceFileName: str,
                   pickleOut: Optional[str] = None,
                   isHelper: bool = False,
                   integrationEnvVars: List[str] = []):
  secretLines = sourceForLoadingSecrets(integrationEnvVars)
  sourceParts: List[str] = []
  if secretLines is None:
    sourceParts.append("import modelbit, sys")
  else:
    sourceParts.append("import modelbit, sys, os")
    _addSpacer(sourceParts)
    sourceParts.append(secretLines)
    _addSpacer(sourceParts)

  if pyProps.namespaceFroms:
    for iAs, iModule in pyProps.namespaceFroms.items():
      sourceParts.append(f"from {iModule} import {iAs}")
  if pyProps.namespaceImports:
    for iAs, iModule in pyProps.namespaceImports.items():
      if iModule == "modelbit" and iAs == "modelbit":
        continue  # Always added already
      if iModule == iAs:
        sourceParts.append(f"import {iModule}")
      else:
        sourceParts.append(f"import {iModule} as {iAs}")
  _addSpacer(sourceParts)

  if pyProps.userClasses:
    revClasses = pyProps.userClasses.copy()
    revClasses.reverse()  # we want to list classes with deepest dependencies first
    sourceParts.append("\n\n".join(revClasses) + "\n\n")

  if pyProps.namespaceConstants and len(pyProps.namespaceConstants) > 0:
    for nName, nValue in pyProps.namespaceConstants.items():
      sourceParts.append(f'{nName} = {nValue}')

  if pyProps.namespaceVars and pyProps.namespaceVarsDesc:
    for nName, nValue in pyProps.namespaceVars.items():
      desc = pyProps.namespaceVarsDesc[nName]
      if isinstance(nValue, InstancePickleWrapper):
        sourceParts.append(
            f'{nName} = modelbit.load_value("data/{nName.lower()}.pkl", {nValue.clsName}) # {desc}')
      else:
        sourceParts.append(f'{nName} = modelbit.load_value("data/{nName.lower()}.pkl") # {desc}')

  if pyProps.customInitCode:
    sourceParts.append("\n" + "\n\n".join(pyProps.customInitCode))

  _addSpacer(sourceParts)
  if pyProps.namespaceFunctions:
    for _, fSource in pyProps.namespaceFunctions.items():
      sourceParts.append(fSource)
      _addSpacer(sourceParts)

  _addSpacer(sourceParts)
  if pyProps.source:
    if not isHelper:
      sourceParts.append("# main function")
    sourceParts.append(pyProps.source)

  if isHelper:
    pass
  elif pickleOut is None:
    sourceParts.append("# to run locally via git & terminal, uncomment the following lines")
    sourceParts.append('# if __name__ == "__main__":')

    cmdArgs = "..."
    imports: List[str] = []
    if pyProps.isAsync:
      imports.append("asyncio")
    if pyProps.isDataFrameMode:
      cmdArgs = "pd.DataFrame(...)"
      imports.append("pandas as pd")

    if len(imports) > 0:
      sourceParts.append(f"#   import {', '.join(imports)}")

    if pyProps.isAsync:
      sourceParts.append(f"#   result = asyncio.run({pyProps.name}({cmdArgs}))")
    else:
      sourceParts.append(f"#   result = {pyProps.name}({cmdArgs})")

    sourceParts.append(f"#   print(result)")
  else:
    cmdArgs = "*(modelbit.parseArg(v) for v in sys.argv[1:])"
    sourceParts.append("# to run locally via git & terminal")
    sourceParts.append('if __name__ == "__main__":')
    sourceParts.append("\n".join([
        f"  {pickleOut} = {pyProps.name}({cmdArgs})",
        f"  if {pickleOut} is not None:",
        f"    modelbit.save_value({pickleOut}, 'data/{pickleOut}.pkl')",
    ]))
  return RuntimeFile(f"{sourceFileName}.py", "\n".join(sourceParts))


def makeCreateJobRequest(job: JobProps):
  return {
      "name": job.name,
      "schedule": job.schedule,
      "saveOnSuccess": job.saveOnSuccess,
      "emailOnFailure": job.emailOnFailure,
      "refreshDatasets": job.refreshDatasets,
      "sourceFile": makeSourceFile(job.rtProps, job.name, pickleOut=job.outVar).asDict(),
      "timeoutMinutes": job.timeoutMinutes,
      "size": job.size,
      "arguments": job.arguments,
  }
