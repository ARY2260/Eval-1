from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    """
    Test table will be storing details regarding the test created by the user
    """
    title = models.CharField(verbose_name=_("Title"), help_text=_("Required"), max_length=255)
    description = models.TextField(verbose_name=_("Description"), help_text=_("Required"), max_length=500)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")
    
    def get_absolute_url(self):
        return reverse("eval:test-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class Question(models.Model):
    """
    Question table will be storing details regarding the question created by the user
    """
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"), help_text=_("Required"))
    question_text = models.TextField(verbose_name=_("Question"), help_text=_("Required"), max_length=500)
    expected_answer = models.TextField(verbose_name=_("Expected Answer"), help_text=_("Required"), max_length=500)
    max_score = models.DecimalField(
        verbose_name=_("Max Score"), 
        help_text=_("Maximum 999.99"), 
        max_digits=5, 
        decimal_places=2
    )

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
    
    def __str__(self):
        return self.question_text


class Examinee(models.Model):
    """
    Examinee table will be storing details regarding the examinee for a given test
    """
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"), help_text=_("Required"))
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"), help_text=_("Required"), max_length=255)
    total_score = models.DecimalField(
        verbose_name=_("Score"), 
        help_text=_("Maximum 999.99"), 
        max_digits=5, 
        decimal_places=2,
        default=None
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, editable=False)

    class Meta:
        verbose_name = _("Examinee")
        verbose_name_plural = _("Examinees")
    
    def __str__(self):
        return self.name


class Submission(models.Model):
    """
    Submission table will be storing details regarding the submission of the examinee
    """
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_("Question"), help_text=_("Required"))
    examinee_id = models.ForeignKey(Examinee, on_delete=models.CASCADE, verbose_name=_("Examinee"), help_text=_("Required"))
    answer = models.TextField(verbose_name=_("Answer"), help_text=_("Required"), max_length=1000)
    score = models.DecimalField(
        verbose_name=_("Score"),
        help_text=_("Maximum 999.99"),
        max_digits=5,
        decimal_places=2,
        default=0
    )

    class Meta:
        verbose_name = _("Submission")
        verbose_name_plural = _("Submissions")
    
    def __str__(self):
        return self.answer