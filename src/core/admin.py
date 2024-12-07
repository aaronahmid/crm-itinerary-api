from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import SimpleListFilter

from .models.user import User
from .models import Customer
from .models import Itinerary


class CurrencyFilter(SimpleListFilter):
    title = "Currency"
    parameter_name = "pricing_currency"

    def lookups(self, request, model_admin):
        # Define your filter options here
        return [
            ("USD", "USD"),
            ("EUR", "EUR"),
            ("GBP", "GBP"),
        ]

    def queryset(self, request, queryset):
        # Filter queryset based on the selected currency
        if self.value():
            return queryset.filter(pricing__currency=self.value())
        return queryset


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "created_by", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at", CurrencyFilter)
    search_fields = (
        "customer__email",
        "created_by__email",
        "location__country",
        "location__city",
    )
    ordering = ("created_at",)
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "created_at")
    search_fields = ("email", "first_name", "last_name", "phone")
    ordering = ("created_at",)
    readonly_fields = ("id", "created_at", "updated_at")


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "created_at",
        "updated_at",
        "last_login",
    )
    list_filter = ("is_staff", "is_active")
    readonly_fields = ("created_at", "updated_at", "last_login")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
