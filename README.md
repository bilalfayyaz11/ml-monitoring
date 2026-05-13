# NLP-Driven Automated Compliance Reporting with ELK Stack

## Objectives
- Deploy and configure a full ELK Stack (Elasticsearch, Logstash, Kibana) on Ubuntu 24.04
- Ingest structured system logs via Logstash with custom Grok parsing
- Visualize compliance log data in Kibana using index patterns and pie chart aggregations
- Apply NLP sentiment analysis to automatically flag compliance-risk log entries
- Export a machine-readable compliance risk report as CSV

## Tools Used
| Tool | Purpose |
|---|---|
| Elasticsearch 7.17.17 | Log storage and search indexing |
| Logstash 7.17.17 | Log ingestion and Grok parsing |
| Kibana 7.17.17 | Log visualization and dashboarding |
| Python 3.12 | NLP scripting |
| NLTK (VADER) | Sentiment analysis on log messages |
| pandas | Log structuring and CSV export |
| scikit-learn | NLP pipeline dependency |
| OpenJDK 17 | JVM runtime for ELK Stack |

## Key Skills Demonstrated
- ELK Stack deployment and service management on Ubuntu
- Logstash pipeline design with custom Grok regex patterns
- Kibana index pattern creation and Terms aggregation visualization
- Python-based log parsing with regex
- Sentiment-driven compliance risk scoring using NLTK VADER
- Automated CSV report generation from structured log data

## Troubleshooting Log
| # | Issue | Root Cause | Fix Applied |
|---|---|---|---|
| 1 | `openjdk-11-jdk` specified in lab | Full JDK unnecessary; JRE sufficient for ELK runtime | Replaced with `openjdk-17-jre-headless` |
| 2 | `pip install` blocked | Ubuntu 24.04 PEP 668 externally-managed-environment restriction | Used `python3 -m venv` virtual environment |
| 3 | `_grokparsefailure` on all log entries | `%{TIMESTAMP_ISO8601}` does not match `YYYY-MM-DD` date-only format | Replaced with raw regex `(?<timestamp>\d{4}-\d{2}-\d{2})` |
| 4 | Hardcoded `<your-username>` placeholder in logstash.conf | Lab left path as literal placeholder | Replaced with `${USER}` for automatic resolution |
| 5 | `CountVectorizer` imported but never used | Dead import in lab's Python script | Removed from script |
