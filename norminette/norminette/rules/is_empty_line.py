from rules import PrimaryRule
import pdb

cs_keywords = ["DO", "WHILE", "FOR", "IF", "ELSE", "SWITCH"]
whitespaces = ["TAB", "SPACE", "NEWLINE"]


class IsEmptyLine(PrimaryRule):
    def __init__(self):
        super().__init__()
        self.priority = 70
        self.scope = []

    def run(self, context):
        """
        Catches empty line
        BUG: Catches end of line token on unrecognized line
        """
        i = 0
        while context.check_token(i, ["SPACE", "TAB"]) is True:
            i += 1
        if context.check_token(i, "NEWLINE") is True or context.peek_token(i) is None:
            i = context.eol(i)
            return True, i
        return False, 0
