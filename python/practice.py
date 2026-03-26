class Student(models.Model):
    id = models.IntegerField(PrimaryKey=True)
    name = models.CharField(max_lenght=225)

class Student_info(models.Model):
    id = models.IntegerField(PrimaryKey=True)
    student_id=models.ForeignKey(Student,related_name='student_id')
    age=models.integerField(max_length=3)
    course=models.CharField(max_length=100,null=True,blank=True)