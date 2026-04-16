# AI Log

## PostgreSQL Configuration

Prompt: Asked Copilot to configure the Django project to use PostgreSQL via a `DATABASE_URL` environment variable stored as a GitHub Codespaces secret, without hard-coding credentials in the repository.

Result: Copilot identified the needed database packages, updated `requirements.txt` to include `dj-database-url` and `psycopg[binary]`, and changed `settings.py` to read `DATABASE_URL` from the environment with a SQLite fallback when the variable is absent.

My changes: Kept the configuration environment-driven, avoided storing any password or connection string in a repository file, and preserved SQLite as a fallback for local development when `DATABASE_URL` is not set.

Verification: Checked the settings and dependency files for the expected `DATABASE_URL` and package entries, confirmed the database config was still using environment-based parsing, and validated that the Django files had no syntax or import errors.

## Django Admin Registration

Prompt: Asked Copilot to register the Mythical Mane models in Django admin and add useful `list_display`, `search_fields`, `list_filter`, and `date_hierarchy` settings where appropriate.

Result: Copilot generated a set of `ModelAdmin` classes in `mythical_mane/admin.py` and registered the main domain models such as `Patient`, `Owner`, `Visit`, `Invoice`, and related join models.

My changes: Kept the registrations focused on the domain models, used simple list/search/filter settings, and avoided adding complex inlines or custom admin methods.

Verification: Ran Django diagnostics on `mythical_mane/admin.py` and confirmed there were no syntax or import errors.

## Patient Access and Admin Permissions

Prompt: Asked why model data was not visible in admin, whether the app needed migrations, and what minimum permissions were needed to edit records.

Result: Copilot identified that the app needed to be added to `INSTALLED_APPS`, explained that the models were unmanaged because they came from an existing database, and clarified that superusers bypass normal permission checks.

My changes: Added `mythical_mane.apps.MythicalManeConfig` to `INSTALLED_APPS` and verified the admin configuration was loading correctly.

Verification: Restarted the Django server and confirmed the app could load in admin; checked the model registration file for errors.

## Patient List View

Prompt: Asked Copilot to create a Django view, URL route, and Tailwind template for listing patients with owner and universe data.

Result: Copilot generated a class-based list view using `Patient.objects.select_related("owner", "universe")`, added a `/patients/` URL pattern, and created a Tailwind-styled table template.

My changes: Kept the view efficient with `select_related`, added pagination, created a dedicated app URLconf, and used a simple responsive table layout with empty-state and pagination UI.

Verification: Ran Django diagnostics on the new view and URL files to confirm there were no syntax errors; reviewed the template structure and related-field access for correctness.