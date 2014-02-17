#!/usr/bin/env python
import os
import sys


def add_path(relative_path, prepend=False):
  def abs_path(*paths):
    return (os.path.abspath(os.path.join(os.path.dirname(__file__), *paths))
            + '/')
  if prepend:
    return sys.path.insert(0, abs_path(relative_path))
  return sys.path.append(abs_path(relative_path))


if __name__ == "__main__":
  add_path('./website/apps')
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")
  from django.core.management import execute_from_command_line
  execute_from_command_line(sys.argv)
