"""
第8章/cms4py_first_generation/app/controllers/students.py
"""

from app.db.action_with_db import ActionWithDb


class index(ActionWithDb):

    async def execute(self, req, res):
        db = self.db
        students = await db(db.student.id > 0).select()
        await res.render("students.html", students=students)
