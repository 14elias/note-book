import { useState } from 'react'
import { BrowserRouter,Route,Routes,Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import NotFound from './pages/NotFound'
import Home from './pages/Home'
import ProtectedRoute from './components/ProtectedRoute'


function LogOut(){
  localStorage.clear()
  return <Navigate to ='/login'/>
}

function RegisterAndLogOut(){
  localStorage.clear()
  return <Register/>
}

function App() {

  return (
  <BrowserRouter>
  <Routes>
    <Route path='/' element={
      <ProtectedRoute>
        <Home/>
      </ProtectedRoute>
    }/>
    <Route path='/login' element={<Login/>}/>
    <Route path='/logout' element={<LogOut/>}/>
    <Route path='/register' element={<RegisterAndLogOut/>}/>
    <Route path='*' element={<NotFound/>}/>
  </Routes>
  </BrowserRouter>
)
}

export default App
