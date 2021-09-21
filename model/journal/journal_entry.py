""" The data recorded in a Journal """
import datetime

from model.data.dollars import Dollars


class JournalEntry:
    """ An entry for an economic event """

    def __init__(self,
                 date: datetime.date,
                 dollars: Dollars,
                 description: str,
                 ):
        self.date = date
        self.dollars = dollars
        self.description = description

    def __str__(self):
        return "| "+str(self.date)+" | "+self.description+" | "+str(self.dollars)
