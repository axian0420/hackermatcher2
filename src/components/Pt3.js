import React from 'react';

function Pt3() {
  return (
    <div className="center">
      <div className="pt3">
        <h2>
          What We Do
        </h2>

        <div className="col-md-2">
          <img
            alt="feat1"
            src={require("../assets/landing_feature_1.png")}
          />

          <h3>
              Customized Matching Algorithm
          </h3>
          <p>
          Any hackathon that you select will
          instantly give you a list of hackers
            that most closely match your interests
            and skill level. Quick and simple! 
          </p>

        </div>

        <div className="col-md-3">
          <img
            alt="feat2"
            src={require("../assets/landing_feature_2.png")}
          />

          <h3>
              Choose Your Team
          </h3>
          <p>
          Want to see a complete list of hackers?
          Our visualization gives you an intuitive view of attendees, 
          with the ability to filter them based on major, graduation year, and hackathon experience.
          </p>
        </div>
        
      </div>
    </div>
  );
}

export default Pt3;
