(()=>{'use strict';
const BRANDS={
 'CT Money':{className:'reward-ct',logo:'https://s201.q4cdn.com/326551073/files/design/triangle-rewards-logo.png'},
 'More Rewards':{className:'reward-more',logo:'https://account.morerewards.ca/static/media/logo-mr.c02471fbbfabf3e6ed37.png'},
 'Scene+':{className:'reward-scene',logo:'https://cdn-ca.aglty.io/project-harmony/scene-logo-hires_20250425033110.png'}
};
function apply(){document.querySelectorAll('#pointProgramCards .profit-card').forEach(card=>{const name=card.querySelector('h3')?.textContent?.trim()||'',b=BRANDS[name];card.classList.add('point-brand-card');card.classList.remove('reward-ct','reward-more','reward-scene');card.style.removeProperty('--brand-image');if(!b)return;card.classList.add(b.className);card.style.setProperty('--reward-logo',`url("${b.logo}")`)})}
const prior=window.renderPointPrograms;window.renderPointPrograms=function(){if(prior)prior();apply()};
new MutationObserver(apply).observe(document.documentElement,{childList:true,subtree:true});
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(apply,100));else setTimeout(apply,100);
})();
