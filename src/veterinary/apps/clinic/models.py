from apps.users.models import User
from django.db import models


class Analysis(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.CharField("Descrpción", max_length=100)
    price = models.DecimalField("Precio", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"

    def __str__(self):
        return self.name


class Treatment(models.Model):
    # treatment_type
    OPTIONAL = 0
    MANDATORY = 1

    TREATMENT_TYPE_CHOICES = (
        (OPTIONAL, "Opcional"),
        (MANDATORY, "Obligatorio"),
    )

    # Periods
    NA = 0
    DIARY = 1
    WEEKLY = 2
    MONTHLY = 3
    BIMONTHLY = 4
    QUARTERLY = 5
    BIYEARLY = 6
    YEARLY = 7

    PERIOD_CHOICES = (
        (NA, "No aplica"),
        (DIARY, "Diario"),
        (WEEKLY, "Semanal"),
        (MONTHLY, "Mensual"),
        (BIMONTHLY, "Bimestral"),
        (QUARTERLY, "Trimestral"),
        (BIYEARLY, "Semestral"),
        (YEARLY, "Anual"),
    )

    name = models.CharField("Nombre", max_length=50)
    description = models.CharField("Descripción", max_length=100)
    treatment_type = models.IntegerField(
        "Tipo", choices=TREATMENT_TYPE_CHOICES, default=0
    )
    price = models.DecimalField("Precio", max_digits=5, decimal_places=2)
    period = models.IntegerField("Periodo", choices=PERIOD_CHOICES, default=0)

    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"

    def __str__(self):
        return self.name


class Hospitalization(models.Model):
    # Hospitalization type
    SURGERY = 1
    URGENCY = 2

    HOSPITALIZATION_TYPE_CHOICES = (
        (SURGERY, "Cirugía"),
        (URGENCY, "Urgencia"),
    )

    name = models.CharField("Nombre", max_length=100)
    hospitalization_type = models.IntegerField(
        "Tipo", choices=HOSPITALIZATION_TYPE_CHOICES, default=0
    )
    price = models.DecimalField("Precio", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Hospitalización"
        verbose_name_plural = "Hospitalizaciones"

    def __str__(self):
        return self.name


class Proprietor(models.Model):
    name = models.CharField("Nombre", max_length=50)
    last_name = models.CharField("Apellido", max_length=50)
    address = models.CharField("Dirección", max_length=100)
    phone = models.CharField("Teléfono", max_length=12)
    email = models.EmailField("Email", max_length=254)

    class Meta:
        verbose_name = "Propieario"
        verbose_name_plural = "Propietarios"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Disease(models.Model):
    name = models.CharField("Nombre", max_length=50)
    description = models.CharField("Descripción", max_length=100)
    mandatory_declaration = models.BooleanField(
        "Declaración obligatoria", default=False
    )

    class Meta:
        verbose_name = "Enfermedad"
        verbose_name_plural = "Enfermedades"

    def __str__(self):
        return self.name


class Pet(models.Model):
    MALE_SEX = "M"
    FEMALE_SEX = "F"

    SEX_CHOICES = (
        (MALE_SEX, "Macho"),
        (FEMALE_SEX, "Hembra"),
    )

    name = models.CharField("Nombre", max_length=50)
    kind = models.CharField("Especie", max_length=50)
    breed = models.CharField("Raza", max_length=30)
    sex = models.CharField("Sexo", max_length=1, choices=SEX_CHOICES)
    birth_date = models.DateField(
        "Fecha de Nacimiento", auto_now=False, auto_now_add=False
    )
    death_date = models.DateField(
        "Fecha de fallecimiento",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    proprietor = models.ForeignKey(
        Proprietor, on_delete=models.CASCADE, related_name="proprietor_of"
    )

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return f"{self.kind} - {self.name}"


class Reception(models.Model):
    register_date = models.DateTimeField(
        "Fecha de registro", auto_now=False, auto_now_add=True
    )
    reason = models.CharField("Motivo", max_length=50)
    condition = models.CharField("Condición", max_length=50)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pet_of")

    class Meta:
        verbose_name = "Recepción"
        verbose_name_plural = "Recepciones"

    def __str__(self):
        return f" Recepción {self.pk} - {self.register_date}"


class Displacement(models.Model):
    displacement_date = models.DateTimeField(
        "Fecha de desplazamiento", auto_now=False, auto_now_add=True
    )
    price = models.DecimalField("Precio", max_digits=5, decimal_places=2)
    alternate_address = models.CharField("Dirección alterna", max_length=100)
    reception = models.ForeignKey(
        Reception, on_delete=models.CASCADE, related_name="reception_with"
    )
    assistant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="assistant_perform"
    )

    class Meta:
        verbose_name = "Desplazamiento"
        verbose_name_plural = "Desplazamientos"

    def __str__(self):
        return f" Desplazamiento {self.pk} - {self.displacement_date}"


class Diagnostic(models.Model):
    diagnostic_date = models.DateTimeField(
        "Fecha de diagnóstico", auto_now=False, auto_now_add=True
    )
    result = models.CharField("Resultado", max_length=100)
    reception = models.ForeignKey(
        Reception, on_delete=models.CASCADE, related_name="reception_in"
    )
    analysis = models.ForeignKey(
        Analysis, on_delete=models.CASCADE, related_name="analysis_of"
    )

    class Meta:
        verbose_name = "Disgnóstico"
        verbose_name_plural = "Diagnósticos"

    def __str__(self):
        return f" Diagnóstico {self.pk} - {self.diagnostic_date}"


class TreatmentApplied(models.Model):

    NORMAL = 1
    URGENT = 2

    TREATMENTAPPLIED_TYPE_CHOICES = (
        (NORMAL, "Normal"),
        (URGENT, "Urgente"),
    )

    treatment_applied_type = models.IntegerField(
        "Tipo de tratamienio aplicado", choices=TREATMENTAPPLIED_TYPE_CHOICES, default=1
    )
    treatment_appied_date = models.DateTimeField(
        "Fecha de tratamiento aplicado", auto_now=False, auto_now_add=False
    )
    observation = models.CharField("Observaciones", max_length=100)
    reception = models.ForeignKey(
        Reception, on_delete=models.CASCADE, related_name="reception_for"
    )
    veterinary = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="veterinay_perform"
    )

    class Meta:
        verbose_name = "Tratamiento aplicado"
        verbose_name_plural = "Tratamientos aplicados"

    def __str__(self):
        return f" Tratamiento aplicado {self.pk} - {self.treatment_appied_date}"


class MandatoryTreatment(models.Model):
    treatment_applied = models.OneToOneField(
        TreatmentApplied,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="treatment_applied_is",
    )
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="treatment_is"
    )
    drug = models.CharField("Fármaco", max_length=30)
    drug_serial = models.CharField("Serie", max_length=30)

    class Meta:
        verbose_name = "Tratamiento obligatorio"
        verbose_name_plural = "Tratamientos obligatorios"

    def __str__(self):
        return (
            f" Tratamiento {self.treatment_applied} - {self.drug} - {self.drug_serial}"
        )


class OptionalTreatment(models.Model):
    treatment_applied = models.OneToOneField(
        TreatmentApplied,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="treatment_applied_for",
    )
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, related_name="treatment_with"
    )

    class Meta:
        verbose_name = "Tratamiento opcional"
        verbose_name_plural = "Tratamientos opcionales"

    def __str__(self):
        return self.treatment_applied


class Internship(models.Model):
    reception = models.OneToOneField(
        Reception,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="reception_to",
    )
    hospitalization = models.ForeignKey(
        Hospitalization, on_delete=models.CASCADE, related_name="hospitalization_for"
    )
    initial_date = models.DateTimeField(
        "Fecha de ingreso", auto_now=False, auto_now_add=True
    )
    final_date = models.DateTimeField(
        "Fecha de egreso", auto_now=False, auto_now_add=False
    )
    room = models.CharField("Habitáculo", max_length=30)

    class Meta:
        verbose_name = "Internado"
        verbose_name_plural = "Internados"

    def __str__(self):
        return f" Internado {self.reception} - {self.room}"


class DicoverDisease(models.Model):
    diagnostic = models.OneToOneField(
        Diagnostic,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="diagnostic_for",
    )
    disease = models.ForeignKey(
        Disease, on_delete=models.CASCADE, related_name="disease_discovered"
    )

    class Meta:
        verbose_name = "Advertencia de enfermedad"
        verbose_name_plural = "Advertencias de enfermedad"

    def __str__(self):
        return f" Advertencia {self.diagnostic} - {self.disease}"


class Invoice(models.Model):
    NORMAL = 1
    SIMPLIFIED = 2

    INVOICE_TYPE_CHOICES = (
        (NORMAL, "Normal"),
        (SIMPLIFIED, "Simplificada"),
    )

    emission_date = models.DateTimeField(
        "Fecha de emisión", auto_now=False, auto_now_add=True
    )
    invoice_type = models.IntegerField(
        "Tipo de factura", choices=INVOICE_TYPE_CHOICES, default=1
    )
    pay_date = models.DateTimeField("Fecha de pago", auto_now=False, auto_now_add=False)
    total = models.DecimalField("Total", max_digits=5, decimal_places=2)
    reception = models.ForeignKey(
        Reception, on_delete=models.CASCADE, related_name="reception_of"
    )

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def __str__(self):
        return self.pk
