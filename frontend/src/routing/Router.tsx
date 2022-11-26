import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from "../pages/Home";
import PageNotFound from "../pages/404";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route index path="/" element={<Home/>}/>
        {/* add your routes here... */}

        <Route path="*" element={<PageNotFound/>}/>
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
