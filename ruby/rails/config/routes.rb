Rails.application.routes.draw do
    match '/', to: 'demo#index', via: :all

    root 'demo#index'
end
