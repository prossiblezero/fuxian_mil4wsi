<!--
 Copyright 2023 Bontempo Gianpaolo

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

To convert the dataset into PyTorch geometric launch:

```bash
python prepare_dataset.py --source PATH --dest PATH --levels 23
```

where levels represent the magnitude scale:
```
1=x5, 2=x10, 3=x20
```
