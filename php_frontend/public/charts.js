document.addEventListener('DOMContentLoaded',()=>{
 const dataEl=document.getElementById('forecast-data');
 if(!dataEl)return;
 const data=JSON.parse(dataEl.textContent||'{}');
 const canvas=document.getElementById('tempChart');
 if(!canvas||!data.daily)return;
 const ctx=canvas.getContext('2d');
 ctx.beginPath();
 data.daily.temperatures.forEach((t,i)=>{
  const x=i*20+10,y=100-t;
  i?ctx.lineTo(x,y):ctx.moveTo(x,y);
 });
 ctx.stroke();
});
