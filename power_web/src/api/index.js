export function login (data) {
  return fetch('/powerBank/login', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function logout (data) {
  return fetch('/powerBank/logout', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function register (data) {
  return fetch('/powerBank/student/register', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function searchStudent (data) {
  return fetch('/powerBank/student/search', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function updateStudent (data) {
  return fetch('/powerBank/student/update', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function addLesson (data) {
  return fetch('/powerBank/lesson/add', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function searchLesson (data) {
  return fetch('/powerBank/lesson/search', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function conductLesson (data) {
  return fetch('/powerBank/lesson/conduct', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function recoverLesson (data) {
  return fetch('/powerBank/lesson/recover', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}
