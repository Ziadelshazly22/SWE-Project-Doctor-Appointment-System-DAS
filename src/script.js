// Simulated database
const users = [
    { username: 'doctor', password: 'password123', role: 'doctor' },
    { username: 'admin', password: 'adminpass', role: 'admin' },
    { username: 'receptionist1', password: 'recpass', role: 'receptionist' },
    { username: 'patient1', password: 'patientpass', role: 'patient' },
];

// Function to handle login
function handleLogin(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    console.log(`Username: ${username}, Password: ${password}, Role: ${role}`);

    // Check user credentials
    const user = users.find(user => user.username === username && user.password === password);

    console.log(`Found User: ${user ? JSON.stringify(user) : 'None'}`);

    if (user && user.role === role) {
        alert(`Login successful as ${role}`);
        // Redirect or perform role-based actions
        window.location.href = `${role}_dashboard.html`;
    } else {
        alert('Invalid username, password, or role. Please try again.');
    }
}

document.getElementById("loginForm")?.addEventListener("submit", handleLogin);

// Mock User Database (for demonstration purposes)
const mockUsers = {
    doctor: { password: "password123", role: "doctor" },
    admin: { password: "adminpass", role: "admin" },
    receptionist1: { password: "recpass", role: "receptionist" },
    patient1: { password: "patientpass", role: "patient" }
};

document.getElementById("registerForm")?.addEventListener("submit", function (event) {
    event.preventDefault();
    alert("Registration request submitted!");
    window.location.href = "index.html";
});