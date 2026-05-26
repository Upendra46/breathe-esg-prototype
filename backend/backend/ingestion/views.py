import json
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import RawRecord


@csrf_exempt
def upload_data(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    file = request.FILES.get("file")
    source = request.POST.get("source")

    if not file or not source:
        return JsonResponse({"error": "file and source required"}, status=400)

    try:
        # SAP / Utility CSV handling
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
            data = df.to_dict(orient="records")

        # JSON handling (Travel data)
        elif file.name.endswith(".json"):
            data = json.load(file)

        else:
            return JsonResponse({"error": "Unsupported format"}, status=400)

        raw = RawRecord.objects.create(
            source=source,
            raw_json=data
        )

        return JsonResponse({
            "message": "Uploaded successfully",
            "record_id": raw.id
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
