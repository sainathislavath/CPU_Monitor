from flask import Flask, request, render_template
import psutil

app = Flask(__name__)

# CPU Threshold
CPU_THRESHOLD = 80  # Example threshold for CPU usage
SAMPLE_INTERVAL = 1  # Sample interval in seconds

# Route for home page
@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    
    if request.method == 'POST':
        try:
            # Measure CPU usage
            usage = psutil.cpu_percent(interval=SAMPLE_INTERVAL)
            
            # Check if CPU usage exceeds the threshold
            if usage > CPU_THRESHOLD:
                message = f"CPU usage exceeded the threshold: {usage}% > {CPU_THRESHOLD}%"
                
            else:
                message = f"CPU usage is within the threshold: {usage}% <= {CPU_THRESHOLD}%"
                
        except Exception as e:
            message = f"An error occurred while monitoring CPU: {str(e)}"
        
    return render_template('index.html', message=message)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
