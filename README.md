# DevPulse — Agile Team Health Dashboard

DevPulse is an internal engineering utility designed to capture daily team metrics, flag blockers, and calculate macro-level health trends without overhead friction.

## Core Architecture
- **Backend**: Django 5.0 + Django REST Framework (Stateless REST API)
- **Frontend**: React + Vite (Single Page Application)
- **Database**: SQLite (Local development) -> PostgreSQL (Production transition)

## Backend Setup & Installation

1. Navigate to the backend application:
   ```bash
   cd backend