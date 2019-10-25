from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField()

    def get_absolute_url(self):
        """
        This method is defined so that it can be called when we are using links to other pages
        The link will look like this <a href="{{instance.get_absolute_url}}"> . In this link an instance is an instance
        of the object that we have in the view template.
        In the urls.py we name each url, then here we call that name and for the dynamic value we assign that using
        self.id, this way the product_id gets replaced.
        The benefit of this is that we are not relying on the urls that we have written in urls.py
        The name will get always the latest ones and then give it the product it.
        This means if I change the product to products, I don't need to update any of my templates urls.
        the product in the reverse refers to the name of the app which is products in this case.
        The app name helps in searching for the url name. so if we have multiple urls named similarly, the use of app
        name will ensure that the reverse function finds the correct one.
        :return:
        """
        return reverse("products:product_details", kwargs={"product_id": self.id})

