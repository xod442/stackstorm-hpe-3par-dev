# (C) Copyright 2019 Hewlett Packard Enterprise Development LP.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# __author__ = "@netwookie"
# __credits__ = ["Rick Kauffman"]
# __license__ = "Apache2.0"
# __maintainer__ = "Rick Kauffman"
# __email__ = "rick.a.kauffman@hpe.com"


from lib.actions import Hpe3ParBaseAction
from datetime import datetime

class Tasks(Hpe3ParBaseAction):
    def run(self):
        # Connect to the system
        api = self.creds
        # Setup some variables
        task_data = []
        # Get the arrays
        allTasks = api.getAllTasks()

        for a in allTasks:

            task = [
                    a['id'],
                    a['type']
                    a['name']
                    a['status']
                    a['startTime']
                    a['finishTime']
                    a['user']
                    ]

            task_data.append(task)
        return task_data
