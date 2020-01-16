export function register (data) {
  return fetch('/powerBank/admin/account/create', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function resetAccount (data) {
  return fetch('/powerBank/admin/account/reset', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function login (data) {
  return fetch('/powerBank/user/account/login', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function logout (data) {
  return fetch('/powerBank/user/account/logout', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}

export function searchAccount (data) {
  return fetch('/powerBank/admin/account/search', {
    method: 'post',
    credentials: 'include',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json;charset=UTF-8'
    })
  })
}
