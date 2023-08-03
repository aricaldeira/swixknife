

__all__ = ('SezimalFileInfo',)


import stat, os, grp, pwd, time
import colorama

from .. import Sezimal, SezimalInteger, SezimalDateTime, sezimal_locale, SezimalLocale

from decimal import Decimal


def _get_ls_colors():
    ls_colors = os.environ['LS_COLORS']

    colors = {}

    for item in ls_colors.split(':'):
        if not item:
            continue

        what, color = item.split('=')

        colors[what] = colorama.ansi.code_to_chars(color)

    return colors


LS_COLORS = _get_ls_colors()

del _get_ls_colors


class SezimalFileInfo:
    def __init__(self, file_name: str, locale: SezimalLocale = None):
        self._permission = '-'
        self._permission_simplified = ''
        self._itens_in_directory = SezimalInteger(0)
        self._user = ''
        self._group = ''
        self._file_size = SezimalInteger(0)
        self._date_time = None
        self._color = ''
        self._suffix = ''
        self._suffix_color = ''
        self._link_to = ''
        self._link_to_suffix = ''
        self._link_to_color = ''
        self.locale = sezimal_locale(locale)

        self.file_name = file_name

    @property
    def file_name(self) -> str:
        return self._file_name

    @file_name.setter
    def file_name(self, file_name: str):
        self._file_name = file_name
        self._get_file_info()

    @property
    def permission(self) -> str:
        return self._permission

    @property
    def permission_simplified(self) -> str:
        return self._permission_simplified

    @property
    def itens_in_directory(self) -> SezimalInteger:
        return self._itens_in_directory

    @property
    def user(self) -> str:
        return self._user

    @property
    def group(self) -> str:
        return self._group

    @property
    def file_size(self) -> SezimalInteger:
        return self._file_size

    @property
    def date_time(self) -> SezimalDateTime:
        return self._date_time

    @property
    def color(self) -> str:
        return self._color

    @property
    def suffix(self) -> str:
        return self._suffix

    @property
    def suffix_color(self) -> str:
        return self._suffix_color

    @property
    def link_to(self) -> str:
        return self._link_to

    @property
    def link_to_suffix(self) -> str:
        return self._link_to_suffix

    @property
    def link_to_color(self) -> str:
        return self._link_to_color

    @property
    def is_directory(self) -> bool:
        return self._permission[0] == 'd'

    @property
    def is_hidden(self) -> bool:
        return self._file_name[0] == '.'

    @property
    def is_link(self) -> bool:
        return self._link_to != ''

    def _simplify_permissions(self):
        def _convert_permission(perm):
            if perm.endswith('x'):
                if perm.startswith('rw'):
                    return '■'
                elif perm.startswith('r'):
                    return '□'
                elif perm[1] == 'w':
                    return '▣'
                else:
                    return '⬚'
            else:
                if perm.startswith('rw'):
                    return '●'
                elif perm.startswith('r'):
                    return '○'
                elif perm[1] == 'w':
                    return '◉'
                else:
                    return '◌'

        if len(self._permission) != 10:
            return

        self._permission_simplified = _convert_permission(self._permission[1:4])
        self._permission_simplified += _convert_permission(self._permission[4:7])
        self._permission_simplified += _convert_permission(self._permission[7:10])

    def _get_file_info(self):
        try:
            stat_info = os.lstat(self.file_name)
        except:
            return

        self._itens_in_directory = SezimalInteger(Decimal(stat_info.st_nlink))

        try:
            self._user = pwd.getpwuid(stat_info.st_uid)[0]
        except KeyError:
            self._user = str(stat_info.st_uid)

        try:
            self._group = grp.getgrgid(stat_info.st_gid)[0]
        except KeyError:
            self._group = str(stat_info.st_gid)

        self._file_size = SezimalInteger(Decimal(str(stat_info.st_size)))
        self._date_time = SezimalDateTime.from_timestamp(Decimal(str(stat_info.st_mtime)))

        #
        # Now, let’s deal with the permissions, file type and color
        #
        if stat.S_ISDIR(stat_info.st_mode):
            self._permission = 'd'
            self._suffix, self._color = self._get_suffix_color(stat_info)

        elif stat.S_ISLNK(stat_info.st_mode):
            self._permission = 'l'
            self._suffix, self._color = self._get_suffix_color(stat_info)
            self._link_to = os.readlink(self.file_name)

            if not os.path.exists(self.file_name):
                self._color = LS_COLORS['or'] if 'or' in LS_COLORS else ''

            else:
                stat_info = os.lstat(self._link_to)
                self._itens_in_directory = SezimalInteger(Decimal(stat_info.st_nlink))
                self._file_size = SezimalInteger(Decimal(str(stat_info.st_size)))
                self._link_to_suffix, self._link_to_color = self._get_suffix_color(stat_info)

                if os.path.isdir(self.file_name):
                    self._permission = 'd'

        elif stat.S_ISBLK(stat_info.st_mode):
            pass
        elif stat.S_ISDOOR(stat_info.st_mode):
            pass
        elif stat.S_ISSOCK(stat_info.st_mode):
            pass
        elif stat.S_ISCHR(stat_info.st_mode):
            pass
        elif stat.S_ISWHT(stat_info.st_mode):
            pass
        elif stat.S_ISFIFO(stat_info.st_mode):
            pass
        elif stat.S_ISPORT(stat_info.st_mode):
            pass
        # elif stat.S_ISGID(stat_info.st_mode):
        #     pass
        # elif stat.S_ISVTX(stat_info.st_mode):
        #     pass

        #
        # Is a regular file
        #
        elif stat.S_ISREG(stat_info.st_mode):
            self._suffix, self._color = self._get_suffix_color(stat_info)

        #
        # Finally, let’s deal with permissions
        #
        for who in 'USR', 'GRP', 'OTH':
            for what in 'R', 'W', 'X':
                if stat.S_IMODE(stat_info.st_mode) & getattr(stat, 'S_I' + what + who):
                    self._permission += what.lower()
                else:
                    self._permission += '-'

        self._simplify_permissions()

    def _get_suffix_color(self, stat_info) -> list[str, str]:
        #
        # Now, let’s deal with the permissions, file type and color
        #
        if stat.S_ISDIR(stat_info.st_mode):
            return ['/', LS_COLORS['di'] if 'di' in LS_COLORS else '']

        elif stat.S_ISLNK(stat_info.st_mode):
            return [' → ', LS_COLORS['ln'] if 'ln' in LS_COLORS else '']

        elif stat.S_ISBLK(stat_info.st_mode):
            pass
        elif stat.S_ISDOOR(stat_info.st_mode):
            pass
        elif stat.S_ISSOCK(stat_info.st_mode):
            pass
        elif stat.S_ISCHR(stat_info.st_mode):
            pass
        elif stat.S_ISWHT(stat_info.st_mode):
            pass
        elif stat.S_ISFIFO(stat_info.st_mode):
            pass
        elif stat.S_ISPORT(stat_info.st_mode):
            pass
        # elif stat.S_ISGID(stat_info.st_mode):
        #     pass
        # elif stat.S_ISVTX(stat_info.st_mode):
        #     pass

        #
        # Is a regular file
        #
        elif stat.S_ISREG(stat_info.st_mode):
            #
            # Let’s check if it is executable
            #
            if stat_info.st_mode & (stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH):
                return ['*', LS_COLORS['ex'] if 'ex' in LS_COLORS else '']

            elif '.' in self.file_name:
                extension = '*.' + self.file_name.split('.')[-1]

                if extension == '*.py':
                    return [' \ufe0f🐍', colorama.ansi.code_to_chars('38:5:106')]

                elif extension == '*.sql':
                    return [' \ufe0f🐘', colorama.ansi.code_to_chars('38:5:102')]

                if extension in LS_COLORS:
                    return ['', LS_COLORS[extension]]

        return ['', '']
