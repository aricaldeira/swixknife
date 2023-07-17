

__all__ = ('SezimalDirectoryList',)


import sys
import os
import colorama


from ..localization import sezimal_locale, SezimalLocale
from .file_info import SezimalFileInfo
from .utils import sezimal_format, decimal_format, dozenal_format


class SezimalDirectoryList:
    def __init__(self, directory_list: list | tuple = None, locale: str | SezimalLocale = None):
        self.locale = sezimal_locale(locale)
        self.show_hidden = False
        self.permissions_simplified = True
        self.date_time_format = None
        self.is_decimal = False
        self.is_dozenal = False
        self.use_prefixes = True
        self.use_dedicated_digits = False
        self.original_path = ''

        if directory_list is None:
            self._get_file_info(os.listdir('.'))
        else:
            self._get_file_info(directory_list)

    def _get_file_info(self, dl: list | tuple = None):
        self._directories = {}
        self._directory_order = []
        self._files = {}
        self._file_order = []

        if not dl:
            return

        for file_name in dl:
            file_info = SezimalFileInfo(file_name, locale=self.locale)

            if file_info.is_directory:
                self._directories[file_info.file_name] = file_info
                self._directory_order.append(file_info.file_name)

            else:
                self._files[file_info.file_name] = file_info
                self._file_order.append(file_info.file_name)

    @property
    def file_list(self):
        res = []

        for file_name in sorted(self._file_order, key=self.locale.sort_key):
            file_info = self._files[file_name]
            file_info.locale = self.locale

            if file_info.is_hidden and not self.show_hidden:
                continue

            res.append(file_info)

        return res

    @property
    def directory_list(self):
        res = []

        for directory_name in sorted(self._directory_order, key=self.locale.sort_key):
            directory_info = self._directories[directory_name]
            directory_info.locale = self.locale

            if directory_info.is_hidden and not self.show_hidden:
                continue

            res.append(directory_info)

        return res

    def _terminal_supports_colors(self, terminal):
        if not hasattr(terminal, 'isatty'):
            return False

        return terminal.isatty()

    def terminal_list(self, terminal=None):
        if terminal is None:
            terminal = sys.stdout

        use_color = self._terminal_supports_colors(terminal)

        lines = []

        user_padding = 0
        group_padding = 0
        size_padding = 0

        for file_info in self.directory_list + self.file_list:
            if file_info.is_hidden and not self.show_hidden:
                continue

            file_info.locale = self.locale

            info = {
                'permission': file_info.permission,
                'file_name': file_info.file_name.replace(self.original_path, ''),
                'suffix': file_info.suffix,
                'link_to': file_info.link_to,
                'user': file_info.user,
                'group': file_info.group,
                'color': file_info.color,
                'date_time': '',
            }

            if self.permissions_simplified:
                info['permission'] = file_info.permission_simplified

            info['date_time'] = file_info.date_time.format(self.date_time_format, locale=self.locale)

            if self.is_decimal:
                if file_info.is_directory:
                    info['size'] = decimal_format(file_info.itens_in_directory, unit='it.', locale=self.locale)
                else:
                    info['size'] = decimal_format(file_info.file_size, unit='B', locale=self.locale, use_prefixes=self.use_prefixes, decimal_places=1)

            elif self.is_dozenal:
                if file_info.is_directory:
                    info['size'] = dozenal_format(file_info.itens_in_directory, unit='it.', locale=self.locale)
                else:
                    info['size'] = dozenal_format(file_info.file_size, unit='B', locale=self.locale, use_prefixes=self.use_prefixes, dozenal_places=1)

            else:
                if file_info.is_directory:
                    info['size'] = sezimal_format(file_info.itens_in_directory, unit='it.', locale=self.locale, use_prefixes=False, dedicated_digits=self.use_dedicated_digits)
                else:
                    info['size'] = sezimal_format(file_info.file_size, unit='B', locale=self.locale, use_prefixes=self.use_prefixes, sezimal_places=1, dedicated_digits=self.use_dedicated_digits)

            user_padding = max(user_padding, len(info['user']))
            group_padding = max(group_padding, len(info['group']))
            size_padding = max(size_padding, len(info['size']))

            lines.append(info)

        for info in lines:
            if use_color:
                line = f'''{info['permission']} {info['user'].ljust(user_padding)} {info['group'].ljust(group_padding)} {info['size'].rjust(size_padding)} {info['date_time']} {info['color']}{info['file_name']}{colorama.Style.RESET_ALL}{info['suffix']}{info['link_to']}\n'''
            else:
                line = f'''{info['permission']} {info['user'].ljust(user_padding)} {info['group'].ljust(group_padding)} {info['size'].rjust(size_padding)} {info['date_time']} {info['file_name']}{info['suffix']}{info['link_to']}\n'''

            terminal.write(line)
