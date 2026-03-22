// 페이지 로드시 로그인 상태 확인
window.onload = function() {
    checkLoginStatus();
}

// 로그인 상태 확인
function checkLoginStatus() {
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');
    const expireTime = localStorage.getItem('tokenExpire');
    const loginBtn = document.querySelector('.login-btn');

    // 토큰 만료 확인
    if (token && expireTime && Date.now() > parseInt(expireTime)) {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        localStorage.removeItem('tokenExpire');
        alert('세션이 만료되었습니다. 다시 로그인해주세요.');
        lockCards();
        loginBtn.textContent = 'Log In';
        loginBtn.onclick = openLogin;
        hideStats();
        return;
    }

    if (token && username) {
        loginBtn.textContent = username + '님 👋';
        loginBtn.onclick = toggleDropdown;
        unlockCards();
        showStats();

        // 자동 로그아웃 예약
        const remaining = parseInt(expireTime) - Date.now();
        setTimeout(() => {
            localStorage.removeItem('token');
            localStorage.removeItem('username');
            localStorage.removeItem('tokenExpire');
            alert('세션이 만료되었습니다. 다시 로그인해주세요.');
            checkLoginStatus();
        }, remaining);

    } else {
        loginBtn.textContent = 'Log In';
        loginBtn.onclick = openLogin;
        lockCards();
        hideStats();
    }
}

// 서버 상태 위젯 표시
async function showStats() {
    document.getElementById('serverStats').classList.add('visible')
    await fetchStats();
    
    // 30초마다 자동 새로고침
    setInterval(fetchStats, 30000);
}

async function fetchStats() {
     const token = localStorage.getItem('token');
    try {
        const response = await fetch('https://api.myhomecloud.kr/system/status', {
            headers: { 'Authorization': 'Bearer ' + token }
        });
        const data = await response.json();
        
        document.getElementById('statStorage').textContent = data.disk.percent + '%';
        document.getElementById('statAI').textContent = 'Deepseek-R1';
        document.getElementById('statServices').textContent = '3 / 3';
        
        // stat-card-sub 업데이트
        const statCards = document.querySelectorAll('.stat-card');
        statCards[0].querySelector('.stat-card-sub').textContent = 
            `${data.disk.used_gb}GB / ${data.disk.total_gb}GB`;
        statCards[1].querySelector('.stat-card-sub').textContent = 
            `CPU ${data.cpu.percent}% · RAM ${data.ram.percent}%`;
    } catch (error) {
        console.error('서버 상태 조회 실패', error);
    }
}

// 서버 상태 위젯 숨기기
function hideStats() {
    document.getElementById('serverStats').classList.remove('visible');
}

// 카드 잠금
function lockCards() {
    const cards = [
        { id: 'card-cloud', url: 'https://cloud.myhomecloud.kr' },
        { id: 'card-code',  url: 'https://code.myhomecloud.kr' },
        { id: 'card-ai',    url: 'https://ai.myhomecloud.kr' }
    ];
    cards.forEach(c => {
        const card = document.getElementById(c.id);
        card.classList.add('locked');
        card.setAttribute('onclick', 'requireLogin()');
        if (!card.querySelector('.lock-icon')) {
            const lock = document.createElement('div');
            lock.className = 'lock-icon';
            lock.textContent = '🔒';
            card.appendChild(lock);
        }
    });
}

// 카드 잠금 해제
function unlockCards() {
    const cards = [
        { id: 'card-cloud', url: 'https://cloud.myhomecloud.kr' },
        { id: 'card-code',  url: 'https://code.myhomecloud.kr' },
        { id: 'card-ai',    url: 'https://ai.myhomecloud.kr' }
    ];
    cards.forEach(c => {
        const card = document.getElementById(c.id);
        card.classList.remove('locked');
        card.setAttribute('onclick', `goTo('${c.url}')`);
        const lock = card.querySelector('.lock-icon');
        if (lock) lock.remove();
    });
}

// 로그인 필요
function requireLogin() {
    openLogin();
}

// 드롭다운 토글
function toggleDropdown() {
    document.getElementById('userDropdown').classList.toggle('active');
}

// 드롭다운 닫기
function closeDropdown() {
    document.getElementById('userDropdown').classList.remove('active');
}

// 비밀번호 변경 모달 열기
function openPasswordChange() {
    closeDropdown();
    document.getElementById('pw-current').value = '';
    document.getElementById('pw-new').value = '';
    document.getElementById('pw-new-confirm').value = '';
    document.getElementById('passwordModal').classList.add('active');
}

// 비밀번호 변경 모달 닫기
function closePasswordChange() {
    document.getElementById('passwordModal').classList.remove('active');
}

// 비밀번호 변경
async function changePassword() {
    const current = document.getElementById('pw-current').value;
    const newPw = document.getElementById('pw-new').value;
    const newPwConfirm = document.getElementById('pw-new-confirm').value;

    if (!current || !newPw || !newPwConfirm) {
        alert('모든 항목을 입력해주세요');
        return;
    }

    if (newPw !== newPwConfirm) {
        alert('새 비밀번호가 일치하지 않습니다 ❌');
        return;
    }

    if (newPw.length < 4) {
        alert('비밀번호는 4자 이상이어야 합니다');
        return;
    }

    const token = localStorage.getItem('token');

    try {
        const response = await fetch('https://api.myhomecloud.kr/auth/password', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({ current_password: current, new_password: newPw })
        });

        const data = await response.json();

        if (response.ok) {
            alert('비밀번호가 변경되었습니다 ✅\n다시 로그인해주세요.');
            closePasswordChange();
            logout();
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert('서버 연결에 실패했습니다');
    }
}
// 로그아웃
function logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('tokenExpire');
    checkLoginStatus();
    alert('로그아웃 되었습니다');
}

// 서비스 이동
function goTo(url) {
    window.location.href = url;
}

// 모달 열기
function openLogin() {
    document.getElementById('loginModal').classList.add('active');
}

// 모달 닫기
function closeLogin() {
    document.getElementById('loginModal').classList.remove('active');
}

// 탭 전환
function switchTab(tab) {
    const loginForm = document.getElementById('form-login');
    const registerForm = document.getElementById('form-register');
    const tabLogin = document.getElementById('tab-login');
    const tabRegister = document.getElementById('tab-register');

    if (tab === 'login') {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
        tabLogin.classList.add('active');
        tabRegister.classList.remove('active');
    } else {
        loginForm.style.display = 'none';
        registerForm.style.display = 'block';
        tabLogin.classList.remove('active');
        tabRegister.classList.add('active');
    }
}

// 로그인
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (!username || !password) {
        alert('아이디와 비밀번호를 입력해주세요');
        return;
    }

    try {
        const response = await fetch('https://api.myhomecloud.kr/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('username', username);
            const expireTime = Date.now() + 60 * 60 * 1000;
            localStorage.setItem('tokenExpire', expireTime);
            closeLogin();
            checkLoginStatus();
            alert('환영합니다, ' + username + '님! 😊');
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert('서버 연결에 실패했습니다');
    }
}

// 회원가입
async function register() {
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;
    const passwordConfirm = document.getElementById('reg-password-confirm').value;

    if (!username || !password || !passwordConfirm) {
        alert('모든 항목을 입력해주세요');
        return;
    }
    

    if (password !== passwordConfirm) {
        alert('비밀번호가 일치하지 않습니다 ❌');
        return;
    }

    if (password.length < 4) {
        alert('비밀번호는 4자 이상이어야 합니다');
        return;
    }

    try {
        const response = await fetch('https://api.myhomecloud.kr/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (response.ok) {
            alert('회원가입 완료! 로그인해주세요 😊');
            switchTab('login');
        } else {
            alert(data.detail);
        }
    } catch (error) {
        alert('서버 연결에 실패했습니다');
    }
}

// 모달 바깥 클릭시 닫기
document.getElementById('loginModal').addEventListener('click', function(e) {
    if (e.target === this) closeLogin();
});

// ESC 키로 모달 닫기
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeLogin();
});

// 드롭다운 바깥 클릭시 닫기
document.addEventListener('click', function(e) {
    const dropdown = document.getElementById('userDropdown');
    const loginBtn = document.querySelector('.login-btn');
    if (!dropdown.contains(e.target) && e.target !== loginBtn) {
        closeDropdown();
    }
});

// 비밀번호 모달 바깥 클릭시 닫기
document.getElementById('passwordModal').addEventListener('click', function(e) {
    if (e.target === this) closePasswordChange();
});
