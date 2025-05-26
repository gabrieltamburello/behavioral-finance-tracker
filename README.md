# Behavioral Finance Habit Tracker for Investors

This project is a Python-based command-line application designed to help investors track their emotional states and decision-making patterns related to their investments. By logging daily market perceptions, personal emotions, and the reasoning behind trades, users can gain insights into their behavioral biases and work towards more disciplined investing.

## Purpose / Motivation

The motivation behind this project is to explore the intersection of behavioral finance and practical software development. It serves as a learning exercise in Python, SQLite database management, and building a useful command-line tool. I am particularly interested in how self-reflection can aid in improving investment discipline.

## Current Status & Next Steps

**Current Progress (as of May 25, 2025):**
* Database schema for `daily_entries` table has been defined and created using SQLite (`database_setup.py`).
* Started development of the main application (`main.py`) to add daily entries.
* Implemented user input and validation (including an "exit" option) for the "overall market mood" field.

**Next Steps:**
* Complete user input for "personal emotional state" and "notes" for a daily entry.
* Implement the SQL `INSERT` functionality to save new daily entries to the database.
* Develop functionality to view past entries.

## Technologies Used

* Python 3
* SQLite
* Git & GitHub (with Codespaces)
