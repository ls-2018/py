import fire
from app.applications import Application
from app.utils.command import init_table


class Program:
    # @staticmethod
    # def run(self):
    #     """run this program"""
    #     Application().start_server()

    def migrate(self, drop=False):
        """
        migrate the database
        """

        print(drop)
        init_table()


if __name__ == '__main__':
    fire.Fire(Program)
