#include "LatinoTrees/AnalysisStep/interface/SkimEventProducer.h"
#include "DataFormats/METReco/interface/MET.h"
#include "DataFormats/METReco/interface/METCollection.h"
#include "DataFormats/METReco/interface/PFMET.h"
#include "DataFormats/METReco/interface/PFMETCollection.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include<vector>
#include "Math/VectorUtil.h"


SkimEventProducer::SkimEventProducer(const edm::ParameterSet& cfg) :
    triggerTag_   ( cfg.getParameter<edm::InputTag>("triggerTag")),
    singleMuData_ ( cfg.getParameter<std::vector<std::string> >("singleMuDataPaths") ),
    singleElData_ ( cfg.getParameter<std::vector<std::string> >("singleElDataPaths") ),
    doubleMuData_ ( cfg.getParameter<std::vector<std::string> >("doubleMuDataPaths") ),
    doubleElData_ ( cfg.getParameter<std::vector<std::string> >("doubleElDataPaths") ),
    muEGData_     ( cfg.getParameter<std::vector<std::string> >("muEGDataPaths") ),
    singleMuMC_   ( cfg.getParameter<std::vector<std::string> >("singleMuMCPaths") ),
    singleElMC_   ( cfg.getParameter<std::vector<std::string> >("singleElMCPaths") ),
    doubleMuMC_   ( cfg.getParameter<std::vector<std::string> >("doubleMuMCPaths") ),
    doubleElMC_   ( cfg.getParameter<std::vector<std::string> >("doubleElMCPaths") ),
    muEGMC_       ( cfg.getParameter<std::vector<std::string> >("muEGMCPaths") ),
    AllEmbed_     ( cfg.getParameter<std::vector<std::string> >("AllEmbedPaths") )
{
    mcLHEEventInfoTag_ = cfg.getParameter<edm::InputTag>("mcLHEEventInfoTag");
    mcGenEventInfoTag_ = cfg.getParameter<edm::InputTag>("mcGenEventInfoTag");
    mcGenWeightTag_    = cfg.getParameter<edm::InputTag>("mcGenWeightTag");
    genParticlesTag_   = cfg.getParameter<edm::InputTag>("genParticlesTag");
    genMetTag_         = cfg.getParameter<edm::InputTag>("genMetTag");
    genJetTag_         = cfg.getParameter<edm::InputTag>("genJetTag");
    muTag_             = cfg.getParameter<edm::InputTag>("muTag" );
    elTag_             = cfg.getParameter<edm::InputTag>("elTag" );
    softMuTag_         = cfg.getParameter<edm::InputTag>("softMuTag" );
    jetTag_            = cfg.getParameter<edm::InputTag>("jetTag" );
    tagJetTag_         = cfg.getParameter<edm::InputTag>("tagJetTag" );
    fatJetTag_         = cfg.getParameter<edm::InputTag>("fatJetTag" );
    pfMetTag_          = cfg.getParameter<edm::InputTag>("pfMetTag" );
    tcMetTag_          = cfg.getParameter<edm::InputTag>("tcMetTag" );
    chargedMetTag_     = cfg.getParameter<edm::InputTag>("chargedMetTag" );
    vtxTag_            = cfg.getParameter<edm::InputTag>("vtxTag" );
    chCandsTag_        = cfg.getParameter<edm::InputTag>("chCandsTag" );
    rhoTag_            = cfg.getParameter<edm::InputTag>("rhoTag" );

    if (cfg.exists("sptTag" )) 
     sptTag_ = cfg.getParameter<edm::InputTag>("sptTag" );
    else 
     sptTag_ = edm::InputTag("","","");
    if (cfg.exists("spt2Tag" )) 
     spt2Tag_ = cfg.getParameter<edm::InputTag>("spt2Tag" );
    else 
     spt2Tag_ = edm::InputTag("","","");

    produces<std::vector<reco::SkimEvent> >().setBranchAlias(cfg.getParameter<std::string>("@module_label"));

    // consumes
    genParticlesT_ = consumes<reco::GenParticleCollection>(genParticlesTag_);
    fatJetHT_      = consumes<pat::JetCollection>(fatJetTag_);
    jetHT_         = consumes<pat::JetCollection>(jetTag_);
    rhoT_          = consumes<double>(rhoTag_);
    tagJetHT_      = consumes<pat::JetCollection>(tagJetTag_);
    pfMetHT_       = consumes<std::vector<pat::MET> >(pfMetTag_);
    vtxHT_         = consumes<reco::VertexCollection>(vtxTag_);
    candsHT_       = consumes<reco::CandidateView>(chCandsTag_);
    if(!(sptTag_  == edm::InputTag(""))) sptHT_   = consumes<edm::ValueMap<float> >(sptTag_);
    if(!(spt2Tag_ == edm::InputTag(""))) spt2HT_  = consumes<edm::ValueMap<float> >(spt2Tag_);
    triggerT_      = consumes<edm::TriggerResults>(triggerTag_);
    muonsT_        = consumes<edm::View<reco::RecoCandidate> > (muTag_);
    softsT_        = consumes<edm::View<reco::RecoCandidate> > (softMuTag_);
    electronsT_    = consumes<edm::View<reco::RecoCandidate> > (elTag_);
    if (!(mcGenEventInfoTag_ == edm::InputTag(""))) GenInfoT_     = consumes<GenEventInfoProduct>(mcGenEventInfoTag_);
    if (!(mcGenWeightTag_    == edm::InputTag(""))) mcGenWeightT_ = consumes<GenFilterInfo>(mcGenWeightTag_); 
    if (!(mcLHEEventInfoTag_ == edm::InputTag(""))) productLHET_  = consumes<LHEEventProduct>(mcLHEEventInfoTag_);
    if (!(genMetTag_ == edm::InputTag(""))) genMetHT_ = consumes<reco::GenMETCollection>(genMetTag_);
    if (!(genJetTag_ == edm::InputTag(""))) genJetHT_ = consumes<reco::GenJetCollection>(genJetTag_);

}


void SkimEventProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {

    std::auto_ptr<std::vector<reco::SkimEvent> > skimEvent(new std::vector<reco::SkimEvent> );

    edm::Handle<reco::GenParticleCollection> genParticles;
    if(!(genParticlesTag_ == edm::InputTag(""))) {
     iEvent.getByToken(genParticlesT_,genParticles);
    }

    edm::Handle<pat::JetCollection> fatJetH;
    iEvent.getByToken(fatJetHT_,fatJetH);

    edm::Handle<pat::JetCollection> jetH;
    iEvent.getByToken(jetHT_,jetH);

    edm::Handle<double> rhoJetIso;
    iEvent.getByToken(rhoT_,rhoJetIso);

    edm::Handle<pat::JetCollection> tagJetH;
    if(!(tagJetTag_==edm::InputTag(""))) iEvent.getByToken(tagJetHT_,tagJetH);

    edm::Handle< std::vector<pat::MET> > pfMetH;
    iEvent.getByToken(pfMetHT_,pfMetH);

    edm::Handle<reco::VertexCollection> vtxH;
    iEvent.getByToken(vtxHT_,vtxH);

    edm::Handle<reco::CandidateView> candsH;
    iEvent.getByToken(candsHT_,candsH);

    edm::Handle<edm::ValueMap<float> > sptH;
    if(!(sptTag_ == edm::InputTag(""))) iEvent.getByToken(sptHT_,sptH);

    edm::Handle<edm::ValueMap<float> > spt2H;
    if(!(spt2Tag_ == edm::InputTag(""))) iEvent.getByToken(spt2HT_,spt2H);

    edm::Handle<edm::TriggerResults> triggerResults;
    iEvent.getByToken(triggerT_,triggerResults);
    // May God have mercy on my soul ...
    std::vector<bool> passBits;
    passBits.push_back( singleMuData_.check(iEvent,*triggerResults) );
    passBits.push_back( singleElData_.check(iEvent,*triggerResults) );
    passBits.push_back( doubleMuData_.check(iEvent,*triggerResults) );
    passBits.push_back( doubleElData_.check(iEvent,*triggerResults) );
    passBits.push_back( muEGData_.check( iEvent,*triggerResults) );
    passBits.push_back( singleMuMC_.check(iEvent,*triggerResults) );
    passBits.push_back( singleElMC_.check(iEvent,*triggerResults) );
    passBits.push_back( doubleMuMC_.check(iEvent,*triggerResults) );
    passBits.push_back( doubleElMC_.check(iEvent,*triggerResults) );
    passBits.push_back( muEGMC_.check( iEvent,*triggerResults) );
    passBits.push_back( AllEmbed_.check( iEvent,*triggerResults) );

    //---- RecoCandidate in order to be used by SKimEvent later in a template way
    edm::Handle<edm::View<reco::RecoCandidate> > muons;
    iEvent.getByToken(muonsT_,muons);
    edm::Handle<edm::View<reco::RecoCandidate> > softs;
    iEvent.getByToken(softsT_,softs);
    edm::Handle<edm::View<reco::RecoCandidate> > electrons;
    iEvent.getByToken(electronsT_,electrons);

    edm::Handle<GenFilterInfo> mcGenWeight;
    if (!(mcGenWeightTag_ == edm::InputTag(""))) {
     iEvent.getByToken(mcGenWeightT_, mcGenWeight);
    }

    edm::Handle<GenEventInfoProduct> GenInfoHandle;
    if (!(mcGenEventInfoTag_ == edm::InputTag(""))) {
      iEvent.getByToken(GenInfoT_, GenInfoHandle);
    }
    edm::Handle<LHEEventProduct> productLHEHandle;
    if (!(mcLHEEventInfoTag_ == edm::InputTag(""))) {
     iEvent.getByToken(productLHET_, productLHEHandle);
    }

    edm::Handle<reco::GenMETCollection> genMetH;
    if (!(genMetTag_ == edm::InputTag(""))) {
    iEvent.getByToken(genMetHT_,genMetH);
    }

    edm::Handle<reco::GenJetCollection> genJetH;
    if (!(genJetTag_ == edm::InputTag(""))) {
    iEvent.getByToken(genJetHT_,genJetH);
    }

    skimEvent->push_back( *(new reco::SkimEvent() ) );

    for(size_t i=0;i<electrons->size();++i) {
     skimEvent->back().setLepton(electrons,i);
    }

    for(size_t k=0;k<muons->size();++k) {
     skimEvent->back().setLepton(muons,k);
    }

    for(size_t k=0;k<softs->size();++k) {
     skimEvent->back().setSoftMuon(softs,k);
    }


    // Everything else
    skimEvent->back().setTriggerBits(passBits);
    skimEvent->back().setJets(jetH);
    skimEvent->back().setFatJets(fatJetH);
    skimEvent->back().setJetRhoIso(rhoJetIso);
    skimEvent->back().setPFMet(pfMetH);
    skimEvent->back().setVertex(vtxH);
    if(sptH.isValid() ) skimEvent->back().setVtxSumPts(sptH);
    if(spt2H.isValid() ) skimEvent->back().setVtxSumPt2s(spt2H);
    if(tagJetH.isValid()) skimEvent->back().setTagJets(tagJetH);
    else skimEvent->back().setTagJets(jetH);

    if(genParticles.isValid()) {
     skimEvent->back().setGenParticles(genParticles);
    }
    if(!(mcGenWeightTag_ == edm::InputTag(""))) {
     skimEvent->back().setGenWeight(mcGenWeight);
    }
    if(!(mcGenEventInfoTag_ == edm::InputTag(""))) {
     skimEvent->back().setGenInfo(GenInfoHandle);
    }
    if(!(mcLHEEventInfoTag_ == edm::InputTag(""))) {
     skimEvent->back().setLHEinfo(productLHEHandle);
    }
    if(!(genMetTag_ == edm::InputTag(""))) {
     skimEvent->back().setGenMet(genMetH);
    }
    if(!(genJetTag_==edm::InputTag(""))) {
     skimEvent->back().setGenJets(genJetH);
    }

    iEvent.put(skimEvent);
}


reco::MET SkimEventProducer::doChMET(edm::Handle<reco::CandidateView> candsH,
        const reco::Candidate* cand1,const reco::Candidate* cand2){
    using namespace std;
    reco::Candidate::LorentzVector totalP4;
    for(reco::CandidateView::const_iterator it= candsH->begin(), ed =candsH->end(); it != ed; ++it){
        if( it->charge() == 0 ) continue;
        if(fabs(ROOT::Math::VectorUtil::DeltaR(it->p4(),cand1->p4())) <=0.1) continue;
        if(fabs(ROOT::Math::VectorUtil::DeltaR(it->p4(),cand2->p4())) <=0.1) continue;
        totalP4 += it->p4();
    }
    totalP4 +=cand1->p4();
    totalP4 +=cand2->p4();
    reco::Candidate::LorentzVector invertedP4(-totalP4);
    reco::MET met(invertedP4,reco::Candidate::Point(0,0,0));
    return met;
}


void SkimEventProducer::addDYMVA(reco::SkimEvent* event){
  float dymva0 = -999;
  float dymva1 = -999;

  if (event->nLep() == 2) {

    size_t index = 0;
    float minPt = 0;
    float eta = 4.7;
    int applyCorrection = 1;
    int applyID = 4;

    float jet1pt = event->leadingJetPt (index, minPt, eta, applyCorrection, applyID);
//     float jet1phi = event->leadingJetPhi(index, minPt, eta, applyCorrection, applyID);

//     double dPhiDiLepJet1 = fabs(event->dPhillLeadingJet(eta, applyCorrection, applyID));
//     double dPhiJet1MET = fabs(deltaPhi(jet1phi, event->pfMetPhi()));
//     double dPhillPfMET = fabs(event->dPhillPfMet());

    if (jet1pt < 15) {
      jet1pt = 15;
//       dPhiDiLepJet1 = -0.1;
//       dPhiJet1MET = -0.1;
    }

//     std::cout << " LT:: dPhiDiLepJet1 = " << dPhiDiLepJet1 << std::endl;
//     std::cout << " LT:: dPhiJet1MET = " << dPhiJet1MET << std::endl;
//     std::cout << " LT:: dPhillPfMET = " << dPhillPfMET << std::endl;

//     float px_rec = event->pfMet()*cos(event->pfMetPhi()) + event->pXll();
//     float py_rec = event->pfMet()*sin(event->pfMetPhi()) + event->pYll();
//     double recoil = sqrt(px_rec*px_rec + py_rec*py_rec);

//     std::cout << " LT:: recoil = " << recoil << std::endl;

//     dymva0 = getDYMVA_v0->getValue(event->nCentralJets(30.0, eta, applyCorrection,applyID),
//                    event->pfMet(),
//                    event->chargedMetSmurf(),
//                    jet1pt,
//                    event->pfMetSignificance(),
//                    dPhiDiLepJet1,
//                    dPhiJet1MET,
//                    event->mTHiggs(event->PFMET));
// 
//     dymva1 = getDYMVA_v1->getValue(event->nCentralJets(30.0, eta, applyCorrection, applyID),
//                    event->projPfMet(),
//                    event->projChargedMetSmurf(),
//                    event->nGoodVertices(),
//                    event->pTll(),
//                    jet1pt,
//                    event->pfMetMEtSig(),
//                    dPhiDiLepJet1,
//                    dPhillPfMET,
//                    dPhiJet1MET,
//                    recoil,
//                    event->mTHiggs(event->PFMET));
  
  }

  event->addUserFloat("dymva0", dymva0);
  event->addUserFloat("dymva1", dymva1);
}


//------------------------------------------------------------------------------
// makeJets
//------------------------------------------------------------------------------
void SkimEventProducer::makeJets(
//                  std::vector<MetUtilities::JetInfo> &iJetInfo,
                 const edm::Handle<pat::JetCollection> &jH,
                 reco::VertexCollection &iVertices)
{
//   iJetInfo.clear();

  pat::JetRefVector jrv;

  jrv.clear();

  for (size_t ijet=0; ijet<jH->size(); ++ijet) {

    jrv.push_back(pat::JetRef(jH,ijet));

    double eta = jrv[ijet]->correctedJet("Uncorrected", "none").eta();
    double energy = jrv[ijet]->correctedJet("Uncorrected", "none").energy();
    double neutralHadronEnergy = jrv[ijet]->correctedJet("Uncorrected", "none").neutralHadronEnergy();
    double neutralEmEnergy = jrv[ijet]->correctedJet("Uncorrected", "none").neutralEmEnergy();
    double chargedHadronEnergy = jrv[ijet]->correctedJet("Uncorrected", "none").chargedHadronEnergy();
    double chargedEmEnergy = jrv[ijet]->correctedJet("Uncorrected", "none").chargedEmEnergy();
    // int nConstituents = jrv[ijet]->correctedJet("Uncorrected", "none").nConstituents();
    int chargedMultiplicity = jrv[ijet]->correctedJet("Uncorrected", "none").chargedMultiplicity();

    if (energy == 0) continue;
    if (neutralHadronEnergy / energy > 0.99) continue;
    if (neutralEmEnergy / energy > 0.99) continue;
    // if (nConstituents < 2) continue;
    if (chargedHadronEnergy / energy <= 0 && fabs(eta) < 2.4) continue;
    if (chargedEmEnergy / energy > 0.99 && fabs(eta) < 2.4) continue;
    if (chargedMultiplicity < 1 && fabs(eta) < 2.4) continue;

//     double lNeuFrac = (energy > 0) ? (neutralEmEnergy + neutralHadronEnergy) / energy : 9999;

//     MetUtilities::JetInfo pJetObject;

//     pJetObject.p4 = jrv[ijet]->p4();
//     pJetObject.mva = jrv[ijet]->userFloat("jetMva");
//     pJetObject.neutFrac = lNeuFrac;

//     iJetInfo.push_back(pJetObject);
  }
}


//------------------------------------------------------------------------------
// makeCandidates
//------------------------------------------------------------------------------
void SkimEventProducer::makeCandidates(std::vector<std::pair<LorentzVector,double> > &iPFInfo,
                       edm::Handle<reco::CandidateView> cH,
                       reco::Vertex *iPV)
{
  iPFInfo.clear();

  for (reco::CandidateView::const_iterator it=cH->begin(), ed=cH->end(); it!=ed; ++it) {

    double pDZ = -999;

    if (iPV != 0) {

      double bsx = iPV->x();
      double bsy = iPV->y();
      double bsz = iPV->z();

      double vx = it->vx();
      double vy = it->vy();
      double vz = it->vz();

      if (vx != 0 || vy != 0 || vz != 0) {

    double px = it->p4().px();
    double py = it->p4().py();
    double pz = it->p4().pz();
    double pt = it->p4().pt();
    
    pDZ = fabs((vz - bsz) - ((vx - bsx)*px + (vy - bsy)*py)/pt * pz/pt);

    if (pDZ == 0) pDZ = -999;
      }
    }

    std::pair<LorentzVector,double> pPFObject(it->p4(), pDZ);

    iPFInfo.push_back(pPFObject);
  }
}


//------------------------------------------------------------------------------
// makeVertices
//------------------------------------------------------------------------------
void SkimEventProducer::makeVertices(std::vector<Vector> &iPVInfo,
                     reco::VertexCollection &iVertices)
{
  iPVInfo.clear();

  for (int i0 = 0; i0<(int)iVertices.size(); i0++) {

    const reco::Vertex *pVertex = &(iVertices.at(i0));

    Vector pVec;

    pVec.SetCoordinates(pVertex->x(), pVertex->y(), pVertex->z());

    iPVInfo.push_back(pVec);
  }
}


//------------------------------------------------------------------------------
// getMvaMet
//------------------------------------------------------------------------------
reco::PFMET SkimEventProducer::getMvaMet(const reco::Candidate *cand1,
                     const reco::Candidate *cand2,
                     reco::Vertex *iPV,
                     reco::PFMETCollection thePfMet)
{
  LorentzVector lVis1 = cand1->p4();
  LorentzVector lVis2 = cand2->p4();

  std::vector<LorentzVector > theLeptons;

  theLeptons.push_back(lVis1);
  theLeptons.push_back(lVis2);

//   std::pair<LorentzVector,TMatrixD> lMVAMetInfo = fMVAMet->GetMet(theLeptons,
//                                   lJetInfo,
//                                   lPFInfo,
//                                   lVtxInfo,
//                                   false);
// 
//   reco::PFMET lDummy;
// 
//   reco::PFMET lMVAMet(lDummy.getSpecific(),
//               thePfMet.at(0).sumEt(),
//               lMVAMetInfo.first,
//               iPV->position());

  reco::PFMET lDummy;

  reco::PFMET lMVAMet = lDummy;

  return lMVAMet;
}


SkimEventProducer::~SkimEventProducer() {
//   delete getDYMVA_v0;
//   delete getDYMVA_v1;
}
void SkimEventProducer::beginJob() { }
void SkimEventProducer::endJob() { }
DEFINE_FWK_MODULE(SkimEventProducer);
