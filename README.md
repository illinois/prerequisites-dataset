# University of Illinois' Course Prerequisites
A collection of the prerequisites for all courses offered by the University of Illinois.

You can download the full dataset as a [CSV file.](./uiuc-prerequisites.csv)

## Data Format
The first row of the CSV file contains column headers. Every other row contains data.

There is a single row for every course. The first cell contains the course code (i.e. "AAS 100" or "CS 125"), the second contains the number of prerequisites that correspond to that course, and all subsequent cells contain the course codes of those prerequisites.

| Course  | PrerequisiteNumber | Prerequisites |   |   |   |
| ------- | ------------------ | - | - | - | - |
| AAS 100 | 0 |   |   |   |   |
| ... |   |   |   |   |   |
| CS 225 | 4 | CS 125 | ECE 220 | CS 173 | MATH 213 |
| ... |   |   |   |   |   |

"Choose one of" prerequisites, where only one of a set of courses are required, are counted as multiple prerequisites in this dataset, and are therefore included in the prerequisite count and the list of prerequisites for each course.

## Data Source
Data was parsed from the 'Description' values of the [Course Catalog](https://github.com/illinois/courses-dataset) dataset.

The script used for parsing can be found in `script/`.
