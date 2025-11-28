// Configuration API
const API_BASE_URL = 'http://localhost:8000/api';

// Classe pour gérer les requêtes API
class ApiClient {
    static async request(endpoint, method = 'GET', data = null, token = null) {
        const headers = {
            'Content-Type': 'application/json',
        };

        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const options = {
            method,
            headers,
        };

        if (data) {
            options.body = JSON.stringify(data);
        }

        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.detail || 'Erreur API');
            }

            return result;
        } catch (error) {
            throw error;
        }
    }

    // Authentification
    static register(userData) {
        return this.request('/auth/register', 'POST', userData);
    }

    static login(credentials) {
        return this.request('/auth/login', 'POST', credentials);
    }

    static getCurrentUser(token) {
        return this.request('/auth/me', 'GET', null, token);
    }

    // Gestion des utilisateurs
    static getAllUsers(token) {
        return this.request('/users', 'GET', null, token);
    }

    static getUser(userId, token) {
        return this.request(`/users/${userId}`, 'GET', null, token);
    }

    static updateUserRoles(userId, roles, token) {
        return this.request(`/users/${userId}/roles`, 'PUT', roles, token);
    }

    static deleteUser(userId, token) {
        return this.request(`/users/${userId}`, 'DELETE', null, token);
    }
}

// Gestion du stockage local
class AuthStorage {
    static setToken(token) {
        localStorage.setItem('access_token', token);
    }

    static getToken() {
        return localStorage.getItem('access_token');
    }

    static setUser(user) {
        localStorage.setItem('user', JSON.stringify(user));
    }

    static getUser() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    }

    static clear() {
        localStorage.removeItem('access_token');
        localStorage.removeItem('user');
    }

    static isAuthenticated() {
        return !!this.getToken();
    }
}

// Gestion des alertes
class AlertManager {
    static show(message, type = 'info', elementId = 'alert-message') {
        const alertElement = document.getElementById(elementId);
        if (!alertElement) return;

        alertElement.className = `alert alert-${type} show`;
        alertElement.textContent = message;

        setTimeout(() => {
            alertElement.classList.remove('show');
        }, 5000);
    }

    static success(message, elementId = 'alert-message') {
        this.show(message, 'success', elementId);
    }

    static error(message, elementId = 'alert-message') {
        this.show(message, 'error', elementId);
    }

    static info(message, elementId = 'alert-message') {
        this.show(message, 'info', elementId);
    }
}

// Utilitaires UI
class UIUtils {
    static redirect(path) {
        window.location.href = path;
    }

    static showLoading(element) {
        element.classList.add('loading');
        element.disabled = true;
    }

    static hideLoading(element) {
        element.classList.remove('loading');
        element.disabled = false;
    }

    static formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' };
        return new Date(dateString).toLocaleDateString('fr-FR', options);
    }

    static getRoleLabel(is_admin, is_employer, is_client) {
        if (is_admin) return 'Administrateur';
        if (is_employer) return 'Employé';
        if (is_client) return 'Client';
        return 'Utilisateur';
    }
}

// Export pour utilisation globale
window.ApiClient = ApiClient;
window.AuthStorage = AuthStorage;
window.AlertManager = AlertManager;
window.UIUtils = UIUtils;
