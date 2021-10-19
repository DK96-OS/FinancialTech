""" The file attributes specific to a Journal """
import datetime

from model.journal.journal_attributes import JournalAttributes


class JournalFileAttributes(JournalAttributes):
    """ Contains the file attributes for a standalone journal """

    def __init__(
            self,
            filename: str,
            encryption_params: tuple[str, str, str],
            journal_name: str,
            opening_date: datetime.date,
            closing_date: datetime.date
    ):
        super(JournalFileAttributes, self).__init__(
            journal_name,
            opening_date,
            closing_date
        )
        self.filename = filename
        self.encryption_params = encryption_params
