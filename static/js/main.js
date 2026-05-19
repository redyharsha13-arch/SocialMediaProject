// ============================
// SOCIALHUB — MAIN JAVASCRIPT
// ============================

// Toggle like via AJAX
function toggleLike(postId, button) {
    const csrfToken = getCookie('csrftoken');
    const likeIcon = button.querySelector('.like-icon');
    const likeCount = document.getElementById('like-count-' + postId);

    fetch('/post/' + postId + '/like/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => response.json())
    .then(data => {
        likeCount.textContent = data.likes_count;
        if (data.liked) {
            likeIcon.textContent = '❤️';
            button.classList.add('liked');
        } else {
            likeIcon.textContent = '🤍';
            button.classList.remove('liked');
        }
        // Small pop animation
        button.style.transform = 'scale(1.2)';
        setTimeout(() => { button.style.transform = 'scale(1)'; }, 150);
    })
    .catch(() => {
        // Fallback: redirect to like URL
        window.location.href = '/post/' + postId + '/like/';
    });
}

// Toggle comments section visibility
function toggleComments(id) {
    const section = document.getElementById(id);
    if (!section) return;
    const isHidden = section.style.display === 'none' || section.style.display === '';
    section.style.display = isHidden ? 'block' : 'none';
    if (isHidden) {
        const input = section.querySelector('.comment-input');
        if (input) input.focus();
    }
}

// Get CSRF cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.slice(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Auto-dismiss alerts after 4 seconds
document.addEventListener('DOMContentLoaded', function() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(40px)';
            setTimeout(() => alert.remove(), 400);
        }, 4000);
    });
});
