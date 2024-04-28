import requests
import time
import torch
import torch.nn as nn
import torch.optim as optim
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define a simple linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(1, 1)  # Input size: 1, output size: 1

    def forward(self, x):
        return self.linear(x)

# Prepare data
x_train = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Define the model, loss function, and optimizer
model = LinearRegression()
criterion = nn.MSELoss()  # Mean Squared Error loss
optimizer = optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent optimizer

# Train the model
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(x_train)
    loss = criterion(outputs, y_train)
    
    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')



current_epoch_time = int(time.time())
test_name = 'test_case_1'
result = 'pass'
expected_result='PyTorch - Google Search'
# Function to capture screenshot
def capture_screenshot(driver, test_name, result):
    if result == 'pass':
        driver.save_screenshot(f'screenshots/{test_name}_pass_{current_epoch_time}.png')
    elif result == 'fail':
        driver.save_screenshot(f'screenshots/{test_name}_fail_{current_epoch_time}.png')


  # Use Selenium for web automation
driver = webdriver.Chrome()  # You need to have chromedriver installed and in PATH
driver.get("https://www.google.com")
# Maximize the browser window
driver.maximize_window()
search_box = driver.find_element("name","q")
search_box.send_keys("PyTorch in python")
search_box.send_keys(Keys.RETURN)
  # Capture result status with assertion
response = requests.get("https://www.google.com")

# Print the webpage title and the captured HTTP status code
print(f"Page Title: {driver.title}")
actual_result=driver.title
print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    try:
        assert actual_result.strip() == expected_result.strip(), f"Test failed: Expected '{expected_result}', but got '{actual_result}'"
        print("Test passed")
    except AssertionError as e:
        print(f"AssertionError: {e}")
        print("Test failed")
        result='fail'


# Execute test steps
# Check test result (pass/fail)
try:
    capture_screenshot(driver, test_name, result)
finally:
    driver.quit()
