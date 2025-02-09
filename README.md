---

# Hypothesis to Anki Sync

## 🔥 Supercharge Your Learning & Memory Retention 🚀

### 🧠 What is this project?
This project automates the process of fetching annotations from [Hypothesis](https://web.hypothes.is/) and syncing them to [Anki](https://apps.ankiweb.net/) as flashcards. It uses the Hypothesis API to retrieve annotations and AnkiConnect to add them as cards to a specified Anki deck. Additionally, it sends you a **daily email summary** of the flashcards created so you can review what you studied right before bed—leveraging **science-backed memory techniques** to ensure long-term retention.

---

## 🌟 Why is this powerful?
### 🚨 The Problem: We Learn, Then We Forget
Most of us consume a massive amount of information daily—books, research papers, articles, notes—but struggle to retain what we learn. Studies show that **without review, people forget nearly 50% of new information within an hour and up to 90% within a week**. This phenomenon, known as the **Forgetting Curve**, means that unless you actively reinforce what you've learned, it fades away.

### 🎯 The Solution: Spaced Repetition & Sleep-Based Memory Consolidation
This project leverages two of the most effective learning techniques:
1. **Spaced Repetition** (via Anki) – Uses scientifically proven intervals to reinforce memories before they fade.
2. **Sleep-Based Learning** – Reviewing information before sleep significantly boosts retention. During deep sleep, your brain **strengthens synaptic connections**, making newly acquired knowledge more permanent. Studies in neuroscience show that people who review information before bed **remember it up to 40% better** than those who review it at other times.

---

## 🛠 What this does ?
✅ **Auto-sync annotations to Anki** – Never manually create flashcards again. Your key insights from Hypothesis are automatically converted into study material.

✅ **Daily email review** – Get a summary of your new flashcards every night to reinforce learning before sleep.

✅ **Effortless knowledge retention** – Beat the forgetting curve with active recall and spaced repetition.

✅ **Boost productivity** – Save time by automating note organization and review.

✅ **Personalized learning** – Only study what *you* found important in your readings.

---

## 🚀 How to Use
1. **Set up Hypothesis & AnkiConnect** on your device.
2. **Run the script** to sync annotations from Hypothesis to Anki.
3. **Receive your daily email summary** and review your notes before bed.
4. **Watch your knowledge retention skyrocket!** 📈

---

## ⚡ Why This Matters
In an age of information overload, learning isn't just about consuming—it's about **retaining and applying knowledge**. This tool ensures that what you read doesn't just fade away, but becomes part of your long-term intellectual arsenal. **The smartest learners aren't the ones who read the most, but the ones who remember and apply what they read.**

💡 Want to stay ahead? Start using this project today and **transform the way you learn.**


## Features

- **Fetch Annotations**: Retrieve annotations from Hypothesis using the API.
- **Create Anki Cards**: Automatically create Anki cards with:
  - **Front**: The annotation text.
  - **Back**: The exact quoted text and a link to the source.
  - **Tags**: Tags from Hypothesis (e.g., `#wikipedia`, `#lion`) and a custom `Hypothesis` tag.
- **Auto-Open Anki**: Opens Anki if it’s not already running.
- **Auto-Close Anki**: Closes Anki after processing annotations.
- **Avoid Duplicates**: Tracks processed annotations to avoid adding duplicates.
- **Daily Email Summary**: Sends an email with a summary of the flashcards created each day.

## Prerequisites

Before using this project, ensure you have the following:

1. **Python 3.x**: Install Python from [python.org](https://www.python.org/).
2. **Anki**: Install Anki from [apps.ankiweb.net](https://apps.ankiweb.net/).
3. **AnkiConnect**: Install the AnkiConnect add-on:
   - Open Anki, go to `Tools > Add-ons > Get Add-ons`.
   - Enter code `2055492159` to install AnkiConnect.
   - Restart Anki.
4. **Hypothesis API Token**: Obtain your API token from Hypothesis:
   - Go to [Hypothesis Developer Tokens](https://hypothes.is/account/developer).
   - Generate a new token and copy it.
5. **Gmail Account**: A Gmail account to send email summaries. Enable [App Passwords](https://myaccount.google.com/apppasswords) for secure access.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/L1ZLe/Hypothesis-to-Anki-Sync
   cd hypothesis-to-anki
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholder API token in the script:
   - Open `hypothesis_to_anki.py`.
   - Replace `API_TOKEN = "TTTTTTTTTTTTTTTTTTTTT"` with your actual Hypothesis API token.

4. Configure email settings:
   - Open `email_sender.py`.
   - Replace `EMAIL_FROM` with your Gmail address.
   - Replace `EMAIL_PASSWORD` with your Gmail app password.

5. (Optional) Replace the group ID:
   - If you want to fetch annotations from a specific Hypothesis group, replace `"group": "TTTTTTTTT"` with your group ID.

## Usage

### Running the Script

1. Run the script manually:
   ```bash
   python3 hypothesis_to_anki.py
   ```

2. The script will:
   - Open Anki if it’s not already running.
   - Fetch new annotations from Hypothesis.
   - Create Anki cards in the `Hypothes.is` deck.
   - Send an email summary of the flashcards created.
   - Close Anki after processing.

### Scheduling the Script

You can schedule the script to run automatically at a specific time (e.g., daily at 11 PM).

#### On Linux (cron):

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to run the script daily at 11 PM:
   ```cron
   0 23 * * * export DISPLAY=:0 && /home/jacob/Desktop/My-Scripts/daily-knowledge-review/myenv/bin/python /home/jacob/Desktop/My-Scripts/daily-knowledge-review/hypothes.is_to_anki.py >> /home/jacob/Desktop/My-Scripts/daily-knowledge-review/cron_output.log 2>&1
   ```

#### On Windows (Task Scheduler):

1. Open Task Scheduler.
2. Create a new task:
   - Set the trigger to daily at 11 PM.
   - Set the action to run `pythonw.exe` with the script path as an argument.

#### On Mac (cron or launchd):

1. Use `cron` (similar to Linux) or `launchd` for scheduling.

## How It Works

1. **Fetch Annotations**:
   - The script uses the Hypothesis API to fetch annotations created after the last run.
   - Annotations are filtered by group (if specified) and sorted by creation date.

2. **Create Anki Cards**:
   - For each annotation, the script creates an Anki card with:
     - **Front**: The annotation text.
     - **Back**: The exact quoted text and a link to the source.
     - **Tags**: Tags from Hypothesis and a custom `Hypothesis` tag.

3. **Avoid Duplicates**:
   - The script tracks processed annotation IDs in `processed_ids.txt` to avoid adding duplicates.

4. **Send Email Summary**:
   - After processing annotations, the script sends an email with a summary of the flashcards created.

5. **Auto-Open and Close Anki**:
   - The script opens Anki if it’s not running and closes it after processing annotations.

## Files

- `hypothesis_to_anki.py`: The main script.
- `email_sender.py`: Handles sending email summaries.
- `last_run.txt`: Stores the timestamp of the last processed annotation.
- `processed_ids.txt`: Stores the IDs of processed annotations to avoid duplicates.

## Troubleshooting

### Common Issues

1. **AnkiConnect Not Running**:
   - Ensure Anki is open and AnkiConnect is installed.
   - Check if AnkiConnect is reachable at `http://localhost:8765`.

2. **Hypothesis API Errors**:
   - Verify that your API token is correct.
   - Check the Hypothesis API status at [Hypothesis Status](https://status.hypothes.is/).

3. **Email Not Sending**:
   - Ensure `email_sender.py` is configured with the correct Gmail credentials.
   - Check your Gmail account for security alerts and allow access.

4. **Anki Not Closing**:
   - Ensure the `psutil` library is installed (`pip install psutil`).
   - If Anki doesn’t close, you can forcefully terminate it by replacing `proc.terminate()` with `proc.kill()` in the script.

### Debugging

- Add debug prints to the script to trace its execution.
- Check the terminal output or `cron_output.log` for errors and warnings.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Example Output

When you run the script, you’ll see output like this:

```
Anki is not running. Opening Anki...
Successfully processed 3 new annotations.
Successfully sent learning summary email.
Closing Anki (PID: 12345)...
```

---
