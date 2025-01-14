# Generated by Django 4.2.15 on 2024-10-15 13:32

from django.db import migrations, models
from django.contrib.postgres.operations import ValidateConstraint
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("posthog", "0514_errortrackingstackframe_context")]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[
                ValidateConstraint(
                    model_name="grouptypemapping",
                    name="group_type_project_id_is_not_null",
                ),
                # We can't use AddConstraintNotValid for UNIQUE CONSTRAINTs such as below, but these two here are
                # actually fine, because UNIQUE CONSTRAINTs are backed by indexes - and we've already created the right
                # indexes CONCURRENTLY in the preceding grouptypemapping_project_backfill migration.
                # We signal safety here with `-- existing-table-constraint-ignore`
                migrations.RunSQL(
                    sql='ALTER TABLE "posthog_grouptypemapping" ADD CONSTRAINT "unique group types for project" UNIQUE ("project_id", "group_type"); -- existing-table-constraint-ignore',
                    reverse_sql='ALTER TABLE "posthog_grouptypemapping" DROP CONSTRAINT "unique group types for project";',
                ),
                migrations.RunSQL(
                    sql='ALTER TABLE "posthog_grouptypemapping" ADD CONSTRAINT "unique event column indexes for project" UNIQUE ("project_id", "group_type_index"); -- existing-table-constraint-ignore',
                    reverse_sql='ALTER TABLE "posthog_grouptypemapping" DROP CONSTRAINT "unique event column indexes for project";',
                ),
            ],
            state_operations=[
                migrations.AlterField(
                    model_name="grouptypemapping",
                    name="project",
                    field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="posthog.project"),
                ),
                migrations.AddConstraint(
                    model_name="grouptypemapping",
                    constraint=models.UniqueConstraint(
                        fields=("project", "group_type"), name="unique group types for project"
                    ),
                ),
                migrations.AddConstraint(
                    model_name="grouptypemapping",
                    constraint=models.UniqueConstraint(
                        fields=("project", "group_type_index"), name="unique event column indexes for project"
                    ),
                ),
            ],
        ),
        migrations.RemoveConstraint(
            model_name="grouptypemapping",
            name="unique group types for team",
        ),
        migrations.RemoveConstraint(
            model_name="grouptypemapping",
            name="unique event column indexes for team",
        ),
    ]
