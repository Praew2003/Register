# Register

1. เป็นเว็บแอพพลิเคชั่นสําหรับบันทึก และแสดงผลรายชื่อวิชาที่ที่เปิดให้ลงทะเบียน
   
   ![image](./img/Screenshot%20(41).png)
   ![image](./img/Screenshot%20(42).png)
2. โดยข้อมูลที่จําเป็นประกอบไปด้วย รายวิชา และหมวดหมู่ของรายวิชา
   ![image](./img/Screenshot%20(43).png)
3. กําหนดให้ รายวิชาประกอบไปด้วย
   - รหัสรายวิชา
   - ชื่อรายวิชา
   - หน่วยกิต
   - ภาคการศึกษา
   - ปีการศึกษา
   - หมวดรายวิชา

```python

class Course(models.Model):

    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    credit = models.IntegerField()
    Semester = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title     
```

4. กําหนดให้ หมวดหมู่รายวิชา ประกอบไปด้วย
   - ชื่อหมวดหมู่ (ศึกษาทั่วไป / เฉพาะ / วิชาเลือก)

```python
class Category(models.Model):
    
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
```
5. กําหนดให้ หนึ่งรายวิชา มีได้แค่หนึ่งหมวดหมู่รายวิชา และในแต่ละหมดหมู่รายวิชาสามารถมีได้หลายรายวิชา
   
```python
  from django.db import models

class Category(models.Model):
    
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category
    
class Course(models.Model):

    code = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    credit = models.IntegerField()
    Semester = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title  
```
6. ความสามารถของระบบในภาพรวม

   - แสดงรายชื่อวิชาทั้งหมดได้
   - แสดงรายชื่อวิชาตามหมวดหมู่รายวิชา

 ![image](./img/Screenshot%20(43).png)

7. หน้าเว็บที่จําเป็นต้องมีคือ
   - หน้าแรก แสดงรายวิชาทั้งหมด
   - หน้าหมวดหมู่
   - หน้าเกี่ยวกับเรา
   - หน้าผู้ดูแลระบบ

 ![image](./img/Screenshot%20(43).png)
 ![image](./img/Screenshot%20(36).png)
 ![image](./img/Screenshot%20(37).png)
 ![image](./img/Screenshot%20(38).png)
 ![image](./img/Screenshot%20(39).png)
 ![image](./img/Screenshot%20(44).png)

