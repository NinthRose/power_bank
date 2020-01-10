export function login (query) {
  return fetch({
    port: 8000,
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
