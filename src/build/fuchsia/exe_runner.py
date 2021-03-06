#!/usr/bin/env python
#
# Copyright 2018 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Deploys and executes a packaged Fuchsia executable on a target."""

import argparse
import logging
import sys

from common_args import AddCommonArgs, ConfigureLogging, \
                        GetDeploymentTargetForArgs
from run_package import RunPackage, RunPackageArgs


def main():
  parser = argparse.ArgumentParser()
  AddCommonArgs(parser)
  parser.add_argument(
      '--child-arg',
      action='append',
      help='Arguments for the executable.',
      default=[])
  parser.add_argument(
      'child_args', nargs='*', help='Arguments for the executable.', default=[])
  args = parser.parse_args()
  ConfigureLogging(args)

  with GetDeploymentTargetForArgs(args) as target:
    target.Start()

    child_args = args.child_arg + args.child_args
    run_package_args = RunPackageArgs.FromCommonArgs(args)
    returncode = RunPackage(args.output_directory, target, args.package,
                            args.package_name, child_args, run_package_args)


if __name__ == '__main__':
  sys.exit(main())
