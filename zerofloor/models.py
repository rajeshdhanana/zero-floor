from django.db import models
import datetime

# Create your models here.

class Flat(models.Model):
    flat_number = models.IntegerField()
    def __str__(self):
        return str(self.flat_number)

class ExpenseType(models.Model):
    expense_type = models.CharField(max_length=512)
    def __str__(self):
        return str(self.expense_type)
    class Meta:
        verbose_name = 'ExpenseType'
        verbose_name_plural = 'ExpenseTypes'

class VendorDetails(models.Model):
    vendor_name = models.CharField(max_length=512)
    vendor_other_details = models.CharField(max_length=1024)
    def __str__(self):
        return str(self.vendor_name)
    class Meta:
        verbose_name = 'Vendor Details'
        verbose_name_plural = 'Vendor Details'

class ApartmentBankAccounts(models.Model):
    account_number = models.CharField(max_length=200)
    account_name = models.CharField(max_length=512)
    bank_branch_name = models.CharField(max_length=512)
    def __str__(self):
        return '%s | %s | %s' % ( self.account_number,self.account_name,self.bank_branch_name)

class MonthlyDetails(models.Model):
    month_data = models.CharField(max_length=200)
    added_on = models.DateField()
    def __str__(self):
        return str(self.month_data)
    
    class Meta:
        verbose_name = 'Monthly Details'
        verbose_name_plural = 'Monthly Details'

class MonthlyCollections(models.Model):
    month_details_id = models.ForeignKey(MonthlyDetails,default=1,on_delete=models.CASCADE)
    collection_date = models.DateField()
    amount = models.FloatField(default=0)
    flat_id = models.ForeignKey(Flat,on_delete=models.CASCADE)
    PAYMENT_MODE_CHOICES = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
    )
    payment_mode = models.CharField(
        max_length = 32,
        choices = PAYMENT_MODE_CHOICES,
        default = 'Cash'
    )
    cheque_date = models.DateField(default=datetime.date.today)
    cheque_number = models.IntegerField(default=0)
    cheque_bank_name = models.CharField(max_length = 512, default='abc')
    dep_bank_id = models.ForeignKey(ApartmentBankAccounts,default=1,on_delete=models.CASCADE) 
    def __str__(self):
        return '%s | %s | %s | %s' % ( self.month_details_id.month_data, self.collection_date,self.amount, self.flat_id.flat_number )

    class Meta:
        verbose_name = 'Monthly Collection'
        verbose_name_plural = 'Monthly Collections'

class MonthlyExpenses(models.Model):
    month_details_id = models.ForeignKey(MonthlyDetails,default=1,on_delete=models.CASCADE)
    expenses_type = models.ForeignKey(ExpenseType, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_of_expenditure = models.DateField()
    PAYMENT_MODE_CHOICES = (
        ('Cash', 'Cash'),
        ('Cheque', 'Cheque'),
    )
    payment_mode = models.CharField(
        max_length = 32,
        choices = PAYMENT_MODE_CHOICES,
        default = 'Cash'
    )
    cheque_date = models.DateField(default=datetime.date.today)
    cheque_number = models.IntegerField(default=0)
    dep_bank_id = models.ForeignKey(ApartmentBankAccounts,default=1,on_delete=models.CASCADE) 
    vendor_info = models.ForeignKey(VendorDetails, on_delete=models.CASCADE)
    def __str__(self):
        return '%s | %s | %s ' % ( self.month_details_id.month_data, self.expenses_type,self.amount )
    
    class Meta:
        verbose_name = 'Monthly Expenses'
        verbose_name_plural = 'Monthly Expenses'

class Report(models.Model):
    report_title = models.CharField(max_length=200)
    def __str__(self):
        return str(self.report_title)