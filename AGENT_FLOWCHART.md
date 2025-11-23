# SmartWork AI Agent Workflow - Visual Flowchart

## Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SMARTWORK AI AGENT PIPELINE                         │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌──────────────────┐
                              │  Raw Data Input  │
                              │  (Files/Tasks)   │
                              └────────┬─────────┘
                                       │
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                    1. DATA COLLECTOR AGENT (Agent Tools)                     │
│                                                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │              Tools:                                                    │  │
│  │  • File Reader Tool → Fetch raw data from files/documents             │  │
│  │  • Data extraction and parsing                                        │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│                          Output: Raw Data                                   │
└──────────────────────────┬───────────────────────────────────────────────────┘
                           │
                           │ Raw Data (Tasks, Files, Activities)
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│              2. INSIGHTS GENERATOR AGENT (Sequential Agent)                  │
│                                                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │              Processing:                                              │  │
│  │  • Receives raw data from Data Collector                             │  │
│  │  • Analyzes task patterns and trends                                │  │
│  │  • Identifies key insights and performance metrics                  │  │
│  │  • Extracts actionable intelligence                                 │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│                 Output: Insights & Pattern Analysis                          │
└──────────────────────────┬───────────────────────────────────────────────────┘
                           │
                           │ Analyzed Insights (Patterns, Metrics, Issues)
                           │
                           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│             3. STANDUP SUMMARIZER AGENT (Sequential Agent)                   │
│                                                                               │
│  ┌────────────────────────────────────────────────────────────────────────┐  │
│  │              Processing:                                              │  │
│  │  • Receives insights from Insights Generator                         │  │
│  │  • Generates list of insights and recommendations                   │  │
│  │  • Produces final "Daily Team Snapshot"                            │  │
│  │  • Formats output for team consumption                             │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
│                                                                               │
│              Output: Daily Team Snapshot & Recommendations                    │
└──────────────────────────┬───────────────────────────────────────────────────┘
                           │
                           │ Final Output
                           │
                           ▼
                    ┌──────────────────┐
                    │  Final Deliverable │
                    │ Daily Team Snapshot │
                    │   + Insights       │
                    │ + Recommendations  │
                    └──────────────────┘
```

## Data Flow Summary

| Stage | Component | Input | Processing | Output |
|-------|-----------|-------|-----------|--------|
| 1 | Data Collector Agent | Raw files/documents | File Reader Tool extracts data | Raw data (structured) |
| 2 | Insights Generator Agent | Raw structured data | Pattern analysis, trend detection | Analyzed insights & metrics |
| 3 | Standup Summarizer Agent | Analyzed insights | Summary generation, formatting | Daily Team Snapshot |

## Component Details

### 1. Data Collector Agent
- **Type**: Agent with Tools
- **Main Tool**: File Reader Tool
- **Responsibility**: Fetch and extract raw data from various sources
- **Output Format**: Structured raw data

### 2. Insights Generator Agent
- **Type**: Sequential Agent
- **Dependencies**: Receives output from Data Collector
- **Responsibilities**:
  - Analyze task patterns and distributions
  - Identify trends and anomalies
  - Extract meaningful insights from raw data
- **Output Format**: Analyzed insights with patterns and metrics

### 3. Standup Summarizer Agent
- **Type**: Sequential Agent
- **Dependencies**: Receives output from Insights Generator
- **Responsibilities**:
  - Generate list of key insights
  - Provide actionable recommendations
  - Create final "Daily Team Snapshot" summary
- **Output Format**: Formatted Daily Team Snapshot with recommendations

## Data Types Between Stages

```
Raw Data Flow:
Files/Documents 
    ↓
Data Collector (extracts) 
    ↓
Structured Raw Data
    ↓
Insights Generator (analyzes)
    ↓
Analyzed Insights & Patterns
    ↓
Standup Summarizer (summarizes)
    ↓
Daily Team Snapshot (Final Output)
```

---
