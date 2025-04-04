#!/usr/bin/env python3

import runner, sys
import boards, tegra

module = sys.modules[__name__]
module.name = 'sanity'

class socs(runner.Test):
    def __call__(self, log, *args, **kwargs):
        log.debug('SoCs:')

        for soc in tegra.socs:
            soc = soc()
            log.debug(f'  {soc}')

class list_boards(runner.Test):
    # boards is already a package, but the above test name is a bit ugly,
    # so we override it here
    __name__ = 'boards'

    def __call__(self, log, *args, **kwargs):
        log.debug('Boards:')

        for board in boards.boards:
            # we cannot instantiate these boards here because that would
            # try to open devices that don't exist and fail
            log.debug(f'  {board.name}')

if __name__ == '__main__':
    runner.standalone(module)
