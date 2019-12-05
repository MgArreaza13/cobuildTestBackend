#!/bin/bash
source environments/development_settings.sh
celery -A todoAppBackend.celery worker --pool=solo -l info