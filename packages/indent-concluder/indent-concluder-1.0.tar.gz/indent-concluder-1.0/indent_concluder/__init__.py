INDENT = 4
SHOW_REASON_OF_FAILURE_FOR_NON_META_ITEM = False
AUTO_CALC_SUCCEED = True


class Item:
    def __init__(self, name, succeed=False, reason='') -> None:
        self.name = name
        self._succeed = succeed
        if not AUTO_CALC_SUCCEED:
            self.succeed = succeed
        self.reason = reason
        self.children: list[Item] = []

    if AUTO_CALC_SUCCEED:
        @property
        def succeed(self):
            if not self.children:
                return self._succeed
            else:
                return all([child.succeed for child in self.children])

    def __str__(self) -> str:
        return self._get_str(0)

    def _get_str(self, indent=0):
        succeed_symbol = '√' if self.succeed else '×'
        meta = not self.children

        indent_str = ' ' * indent

        if self.succeed:
            self_str = '{}{} {}'.format(indent_str, self.name, succeed_symbol)
        else:
            if meta:
                self_str = '{}{} {}: {}'.format(indent_str, self.name, succeed_symbol, self.reason)
            else:
                self_str = '{}{} {}: {}'.format(indent_str, self.name, succeed_symbol, '' if not SHOW_REASON_OF_FAILURE_FOR_NON_META_ITEM else self.reason)

            if not meta:
                child_indent = indent + INDENT
                child_strs = [child._get_str(child_indent) for child in self.children]
                child_str = '\n'.join(child_strs)

                self_str += '\n' + child_str

        return self_str

    def append(self, child: 'Item'):
        self.children.append(child)
