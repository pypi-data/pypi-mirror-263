from contextlib import contextmanager
from threading import Lock
from typing import Dict

_exclusive = Lock()
_locks: Dict[str, Lock] = {}


@contextmanager
def _runExclusive():
  global _exclusive
  _exclusive.acquire()
  try:
    yield
  finally:
    _exclusive.release()


def _fetchLock(name: str) -> Lock:
  global _locks
  with _runExclusive():
    if name not in _locks:
      _locks[name] = Lock()
    return _locks[name]


def isLocked(name: str) -> bool:
  return _fetchLock(name).locked()


@contextmanager
def namedLock(name: str):
  namedLock = _fetchLock(name)
  try:
    namedLock.acquire()
    yield
  finally:
    namedLock.release()
