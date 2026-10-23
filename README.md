
# Story Time – Story Management and Web Log Analysis

This project was developed as my **Bachelor's Thesis at Al Akhawayn University, Morocco (2023)**.

Story Time is a static website that allows users to browse and read stories organized by categories and tags. It integrates Python-based content management, customizable page styling, and Apache access log analysis to identify and display the ten most viewed stories.

## Features

### 1. Story Management
- Generate HTML story pages automatically from structured text files.
- Extract story titles, publication dates, tags, and content.
- Maintain a library of available stories and tags.
- Generate dedicated pages for each tag, linking to related stories.
- Update generated pages when the story collection changes.

### 2. Apache Log Analysis
- Parse Apache access logs to identify story visits.
- Count the number of views for each story.
- Rank stories based on their view counts.
- Generate a Top 10 Stories page featuring the most viewed available stories.

### 3. Page Customization
- Customize story title, text, background, tag, and border colors.
- Select colors through a Tkinter graphical interface or the command line.
- Apply selected colors by updating CSS properties.

## Technologies

- **Python:** Story processing, HTML generation, log analysis, and page customization.
- **HTML/CSS:** Website structure and styling.
- **Apache (WAMP):** Local web hosting and access logging.
- **Tkinter:** Graphical interface for color customization.

## Project Structure

```text
static-blog-management-system/
├── Content/                 # Story text files
├── HTMLFiles/               # Generated story and tag pages
├── MainFiles/               # Website pages and stylesheets
├── integrate.py             # Story integration
├── update.py                # Story and library generation
├── views.py                 # Apache log analysis and ranking
├── stylePage.py             # Page styling interface
├── stylingStories.css       # Story page styling
├── stylingTags.css          # Tag page styling
└── requirements.txt         # Python dependencies
```

## Installation and Usage

### 1. Set Up the Project

Install WAMP Server and place the project directory inside:

```text
C:\wamp64\www\static-blog-management-system
```

Create and activate a Python virtual environment:

```bash
python -m venv myenv
myenv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 2. Generate Story Pages

Story files are stored in the `Content` directory and follow this structure:

```text
TITLE
The Power of Kindness
DATE
20/10/2023
TAG
#Kindness #Family

Once upon a time...
```

To generate the story pages, tag pages, and library:

```bash
python update.py
```

To integrate a story using its filename:

```bash
python integrate.py
```

### 3. Generate the Top 10 Stories

Run:

```bash
python views.py
```

The script processes Apache access logs, counts story views, and updates the Top 10 Stories page based on the rankings.

### 4. Customize Story Pages

Run:

```bash
python stylePage.py
```

Choose between command-line styling and the Tkinter graphical interface to customize the appearance of story pages.

### 5. Access the Website

Start Apache through WAMP Server and open:

```text
http://localhost/static-blog-management-system/MainFiles/home.HTML
```

## Project Overview

The project combines static web development with Python automation and web server log analysis. It demonstrates how story content can be transformed into interconnected HTML pages, organized through tags, and ranked using visitor activity recorded in Apache access logs.
