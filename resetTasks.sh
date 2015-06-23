#!/bin/bash
echo "Reset Tasks"
pbs delete_tasks
pbs add_tasks --tasks-file tasks_file.json --tasks-type=json
pbs update_project

