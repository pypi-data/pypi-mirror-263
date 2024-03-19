Change History
**************

0.4.4 (2024-03-19)
==================

- Adapt imports to moved path in slapos.recipe.build

0.4.3 (2021-10-01)
==================

- Clean up part location to make ``install()`` idempotent

- Check url and version mutually exclusive options are not both in options

- Fix version comparison for major version greater than 9

- Remove hardcoded/meaningless/old version number in the path

- Style: import ``UserError`` and use ``Recipe().install()`` one-liner

0.4.2 (2021-07-15)
==================

- Fix encoding error in Python2 by using ``subprocess.checkoutput`` method with
  ``universal_newlines`` option

- Store ``gem dependency`` commands return value in files instead of dictionnary

- Fix gems constraints detection failures for similar version symbol '~>' by
  extending the regex

- Fix gem search pattern for RubyGems >= 3.0.0 by trimming symbols '/' and '\'

- Handle version exclusion constraint symbol '!='

0.4.1 (2021-06-24)
==================

- Add ``allow-picked-version`` as default value for deployment mode.

0.4.0 (2021-06-17)
==================

- Add deployment mode.
- setup: define test dependencies with extras_require [test]
  (instead of deprecated tests_require).

0.3.0 (2020-10-29)
==================

- Project is hosted and maintained by Nexedi;
  URL changed to https://lab.nexedi.com/nexedi/rubygemsrecipe

- Workaround for shebang length limit

- Add support for RubyGems >= 2.0.0 by replacing
  --no-rdoc & --no-ri with --no-document

- Fix Python 3 support by replacing hexagonit.recipe.download dependency
  with slapos.recipe.build

0.2.2 (2015-08-18)
==================

- Fix: https://bitbucket.org/sirex/rubygemsrecipe/issues/8/cant-find-latest-rubygems-version (thanks Pierre Allix)

0.2.1 (2014-11-21)
==================

- Fix: https://bitbucket.org/sirex/rubygemsrecipe/issue/6/cannot-install-rubygems-020

0.2.0 (2014-11-20)
==================

- Native Python 2 and Python 3 support using ``six``, without ``use_2to3``.

- Tests for Python 2 and Python 3 using ``tox`` with 100% test coverage.

- All ``subprocess`` commands are rewritten to run without ``shell=True``.

0.1.8 (2014-01-26)
==================

- Feature: Python 3 support.

- Feature: added 'url', 'gem-options' and 'environment' options.

- Fix: add quotes to values of environment variables.

0.1.7 (2012-05-24)
==================

- Feature: added 'ruby-executable' option, thanks to desaintmartin.

0.1.6 (2012-04-26)
==================

- Fix: pass all arguments as separate arguments instead of a single string.

0.1.5 (2012-01-06)
==================

- Fix: use each version only for the line it's specified in.

0.1.4 (2012-01-03)
==================

- You can specify a version for each gem with a syntax similar to python eggs.


0.1.3 (2011-12-28)
==================

- Added 'version' option to specify explicit rubygems version.

0.1.2 (2011-11-09)
==================

- New version of rubygems includes symlinks in .tgz archyve and extracted by
  setuptools.archive_util extractor ignores all symlinks. This causes missing
  files in extracted folder. Now rubygemsrecipe downloads .zip archyve instead
  of .tgz.

0.1.1 (2011-10-04)
==================

- Fixed issue with name of gem executable, which can be different depending on
  how ruby is istalled on host system.

- Install rubygems if gem executable is not found, not rubygems direcotry.

0.1 (2011-09-07)
================

- Initial public release.
