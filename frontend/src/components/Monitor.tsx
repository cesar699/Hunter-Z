
import {useEffect,useRef} from 'react';import * as echarts from 'echarts';
export default function Monitor(){const ref=useRef(null);useEffect(()=>{if(!ref.current)return;const chart=echarts.init(ref.current);return()=>chart.dispose();},[]);return <div style={{height:260}} ref={ref}/>;}
