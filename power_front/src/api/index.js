export function login (query) {
  return fetch({
    url: '/powerBank/user/account/login',
    method: 'post',
    data: query
  })
}

export function register (query) {
  return fetch({
    url: '/powerBank/admin/account/create',
    method: 'post',
    data: query
  })
}

export function resetAccount (data) {
  return fetch('/powerBank/admin/account/reset', {
    method: 'post',
    body: JSON.stringify(data),
    headers: new Headers({
      'Content-Type': 'application/json'
    })
  })
}
