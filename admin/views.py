# -*- coding: utf-8 -*-

import sys
import subprocess
from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf.global_settings import LANGUAGES
from csskp.settings import BASE_DIR
from survey.lib.utils import export_survey
from survey.models import SurveyUser


@login_required
def export_survey_json(request):
    """Returns the survey (questions, answers, recommendations and sections) in JSON."""
    result = export_survey()
    return JsonResponse(result, safe=False)


@login_required
def survey_status_count(request):
    """Returns the count for the SurveyUser status property."""
    result = SurveyUser.objects.values("status").annotate(count=Count("status"))
    status = {1: "In progress", 2: "Under revies", 3: "Finished"}
    return JsonResponse(
        {status[item["status"]]: item["count"] for item in result.all()}
    )


@login_required
def survey_language_count(request):
    """Returns the count for the SurveyUser choosen_lang property."""
    result = SurveyUser.objects.values("choosen_lang").annotate(
        count=Count("choosen_lang")
    )
    return JsonResponse(
        {
            [lang for lang in LANGUAGES if lang[0] == item["choosen_lang"]][0][1]: item[
                "count"
            ]
            for item in result.all()
        }
    )


@login_required
def site_stats(request):
    """Returns the page which will display some statistics."""
    nb_finished_surveys = SurveyUser.objects.filter(status=3).count()
    nb_surveys = SurveyUser.objects.count()
    context = {"nb_surveys": nb_surveys, "nb_finished_surveys": nb_finished_surveys}
    return render(request, "admin/site_stats.html", context=context)


@login_required
def compile_translations(request):
    """Triggers the compilation of the translation files in a subprocess."""
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "compilemessages",
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR)
    messages.info(request, "Compiled translations files migrated.")
    return HttpResponseRedirect("/admin/")


@login_required
def migrate_database(request):
    """Triggers the execution of the database migration scripts."""
    cmd = [
        sys.exec_prefix + "/bin/python",
        "manage.py",
        "migrate",
    ]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR)
    messages.info(request, "Database up-to-date.")
    return HttpResponseRedirect("/admin/")


@login_required
def update_software(request):
    """Triggers the execution of the script which will update the software."""
    cmd = ["./contrib/update.sh"]
    subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR)
    messages.info(request, "Updated.")
    return HttpResponseRedirect("/admin/")
