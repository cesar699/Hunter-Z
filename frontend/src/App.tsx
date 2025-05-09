
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import UploadPage from './pages/UploadPage';
import TaskPage from './pages/TaskPage';
import MonitorPage from './pages/MonitorPage';
import SideNav from './layouts/SideNav';
import './i18n';

function App(){
  return (
    <BrowserRouter>
      <SideNav/>
      <Routes>
        <Route path="/upload" element={<UploadPage/>}/>
        <Route path="/tasks" element={<TaskPage/>}/>
        <Route path="/monitor" element={<MonitorPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}
export default App;
