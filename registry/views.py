from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .forms import RegistryRecordForm
from .models import RegistryRecord


@require_http_methods(["GET", "POST"])
def registry_page(request):
    if request.method == "POST":
        form = RegistryRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registry:page")
    else:
        form = RegistryRecordForm()

    records = RegistryRecord.objects.all()
    return render(request, "registry/registry.html", {"form": form, "records": records})


@require_http_methods(["POST"])
def delete_record(request, record_id: int):
    record = get_object_or_404(RegistryRecord, id=record_id)
    record.delete()
    return redirect("registry:page")
